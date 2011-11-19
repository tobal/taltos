
import pygame
from pygame.locals import *

import MainExceptions
from src.RpgModules import Sprite
from src.RpgModules import SceneBuilder
from src.RpgModules import RpgTalker
from src.RpgModules import Action
from src.RpgModules import Tram
from src.CommonModules.Constants import RpgModes
from src.CommonModules.Constants import RpgScenes
from src.CommonModules.Constants import Directions
from src.CommonModules.Constants import TunnelData
from src.CommonModules.Constants import CollisionData
from src.CommonModules.Constants import DrawingOrder
from src.CommonModules.Constants import Axis

class Rpg(object):

    def __init__(self, screen, resolution, language):
        self.screen = screen
        self.resolution = resolution
        self.language = language
        
        self.makeScene()
        self.makeSprite()
        
        self.talk = RpgTalker.RpgTalker()
        self.moveX, self.moveY = 0, 0
        self.anim = 0
        if self.scene.isThereTram():
            self.villamos = Tram.Tram()
        self.mode = RpgModes.WANDER
        self.arrowButtons = {Directions.UP : 0,
                             Directions.DOWN : 0,
                             Directions.LEFT : 0,
                             Directions.RIGHT : 0}

    def gameLoop(self):
        self.eventHandler()
        if self.mode == RpgModes.WANDER:
            self.animation()
        tunnel = self.tunnelCheck(self.bulcsu.getBoundingBox())
        if tunnel[TunnelData.TRANSITION]:
            self.changeScene(tunnel[TunnelData.SCENENAME], tunnel[TunnelData.DROPOFF])
        self.collisions()
        if self.scene.isThereTram():
            self.villamos.loop()

        # drawing the whole scene
        self.scene.drawBackGround(self.screen)
        self.scene.drawObjects(DrawingOrder.BACK, self.bulcsu.getBoundingBox().getHorizontalCenter(), self.screen)
        self.screen.blit(self.bulcsu.getCurrentSprite(), (self.bulcsu.getPosX(), self.bulcsu.getPosY()))
        self.scene.drawObjects(DrawingOrder.FRONT, self.bulcsu.getBoundingBox().getHorizontalCenter(), self.screen)
        if self.scene.isThereTram():
            self.villamos.draw(self.screen)
        if self.mode == RpgModes.TALK:
            self.talk.draw(self.screen)

        # for debug purposes
        """
        for obj in self.scene.get_objects():
            box = obj.get_bounding_box().get_box()
            pygame.draw.rect(self.screen, (0,255,0), Rect((box["x1"],box["y1"]), (box["x2"]-box["x1"],box["y2"]-box["y1"])))
        for pers in self.scene.get_persons():
            box = pers.get_bounding_box().get_box()
            pygame.draw.rect(self.screen, (255,0,0), Rect((box["x1"],box["y1"]), (box["x2"]-box["x1"],box["y2"]-box["y1"])))
        for tunnel in self.scene.get_tunnels():
            box = tunnel.get_bounding_box().get_box()
            pygame.draw.rect(self.screen, (0,0,255), Rect((box["x1"],box["y1"]), (box["x2"]-box["x1"],box["y2"]-box["y1"])))
        for action in self.scene.get_actionpoints():
            box = action.get_bounding_box().get_box()
            pygame.draw.rect(self.screen, (255,0,255), Rect((box["x1"],box["y1"]), (box["x2"]-box["x1"],box["y2"]-box["y1"])))
        box = self.bulcsu.get_bounding_box().get_box()
        pygame.draw.rect(self.screen, (255,255,0), Rect((box["x1"],box["y1"]), (box["x2"]-box["x1"],box["y2"]-box["y1"])))
        """

    def makeScene(self):
        # making scene instances
        self.scenes = {RpgScenes.HARDWARE : SceneBuilder.buildScene(RpgScenes.HARDWARE),
                       RpgScenes.STREET : SceneBuilder.buildScene(RpgScenes.STREET),
                       RpgScenes.SHOP : SceneBuilder.buildScene(RpgScenes.SHOP)}
        self.scene = self.scenes[RpgScenes.HARDWARE]

    def changeScene(self, scene, dropoffPoint):
        self.scene = self.scenes[scene]
        self.bulcsu.setPos(dropoffPoint)
        # here is a very temporary and very disgusting solution to the tram-problem
        if self.scene.isThereTram():
            if scene == RpgScenes.STREET:
                offset = -1024
            elif scene == RpgScenes.HARDWARE:
                offset = 1024
            self.villamos.modifyPos(offset)

    def makeSprite(self):
        # making sprite instance
        self.bulcsu = Sprite.ProtagonistSprite(80, 340)

    def eventHandler(self):
        if self.mode == RpgModes.WANDER:
            moveSpeed = 5.5

            for event in pygame.event.get():
                if event.type == QUIT:
                    raise MainExceptions.Exit()
                if event.type == KEYDOWN:
                    if (event.key == K_a) or (event.key == K_LEFT):
                        self.arrowButtons[Directions.LEFT] = 1
                    if (event.key == K_d) or (event.key == K_RIGHT):
                        self.arrowButtons[Directions.RIGHT] = 1
                    if (event.key == K_w) or (event.key == K_UP):
                        self.arrowButtons[Directions.UP] = 1
                    if (event.key == K_s) or (event.key == K_DOWN):
                        self.arrowButtons[Directions.DOWN] = 1
                    if (event.key == K_q) or (event.key == K_ESCAPE):
                        raise MainExceptions.Exit()
                    if (event.key == K_e) or (event.key == K_RETURN):
                        self.action()
                if event.type == KEYUP:
                    if (event.key == K_a) or (event.key == K_LEFT):
                        self.arrowButtons[Directions.LEFT] = 2
                    if (event.key == K_d) or (event.key == K_RIGHT):
                        self.arrowButtons[Directions.RIGHT] = 2
                    if (event.key == K_w) or (event.key == K_UP):
                        self.arrowButtons[Directions.UP] = 2
                    if (event.key == K_s) or (event.key == K_DOWN):
                        self.arrowButtons[Directions.DOWN] = 2

            if self.arrowButtons[Directions.LEFT] == 1:
                if self.moveX == 0:
                    self.moveX = -moveSpeed
                    self.bulcsu.go(Directions.LEFT)
            if self.arrowButtons[Directions.RIGHT] == 1:
                if self.moveX == 0:
                    self.moveX = moveSpeed
                    self.bulcsu.go(Directions.RIGHT)
            if self.arrowButtons[Directions.UP] == 1:
                if self.moveY == 0:
                    self.moveY = -moveSpeed
                    if self.moveX == 0:
                        self.bulcsu.go(Directions.UP)
            if self.arrowButtons[Directions.DOWN] == 1:
                if self.moveY == 0:
                    self.moveY = moveSpeed
                    if self.moveX == 0:
                        self.bulcsu.go(Directions.DOWN)
            if self.arrowButtons[Directions.LEFT] == 2:
                if self.moveX < 0:
                    self.moveX = 0
                    self.bulcsu.stop(Directions.LEFT)
                self.arrowButtons[Directions.LEFT] = 0
            if self.arrowButtons[Directions.RIGHT] == 2:
                if self.moveX > 0:
                    self.moveX = 0
                    self.bulcsu.stop(Directions.RIGHT)
                self.arrowButtons[Directions.RIGHT] = 0
            if self.arrowButtons[Directions.UP] == 2:
                if self.moveY < 0:
                    self.moveY = 0
                    if self.moveX == 0:
                        self.bulcsu.stop(Directions.UP)
                self.arrowButtons[Directions.UP] = 0
            if self.arrowButtons[Directions.DOWN] == 2:
                if self.moveY > 0:
                    self.moveY = 0
                    if self.moveX == 0:
                        self.bulcsu.stop(Directions.DOWN)
                self.arrowButtons[Directions.DOWN] = 0

        if self.mode == RpgModes.TALK:
            for event in pygame.event.get():
                if event.type == QUIT:
                    raise MainExceptions.Exit()
                if event.type == KEYDOWN:
                    if event.key == K_w or event.key == K_UP:
                        self.talk.arrowUp()
                    if event.key == K_s or event.key == K_DOWN:
                        self.talk.arrowDown()
                    if (event.key == K_q) or (event.key == K_ESCAPE):
                        raise MainExceptions.Exit()
                    if (event.key == K_e) or (event.key == K_RETURN):
                        self.action()
                if event.type == KEYUP:
                    if event.key == K_w or event.key == K_UP:
                        return
                    if event.key == K_s or event.key == K_DOWN:
                        return

    def animation(self):
        animSpeed = 6
        animated = False

        if self.moveX > 0:
            self.anim += 1
            animated = True
            if self.anim > animSpeed:
                self.bulcsu.go(Directions.RIGHT)
                self.anim = 0
        elif self.moveX < 0:
            self.anim += 1
            animated = True
            if self.anim > animSpeed:
                self.bulcsu.go(Directions.LEFT)
                self.anim = 0

        if self.moveY > 0:
            if not animated:
                self.anim += 1
            if self.anim > animSpeed:
                if self.moveX == 0:
                    self.bulcsu.go(Directions.DOWN)
                self.anim = 0
        elif self.moveY < 0:
            if not animated:
                self.anim += 1
            if self.anim > animSpeed:
                if self.moveX == 0:
                    self.bulcsu.go(Directions.UP)
                self.anim = 0

    def collisionCheck(self, direction, bulcsuBox):
        objCollision = {CollisionData.COLLISION : False,
                        CollisionData.POSITION : 0}
        for obj in self.scene.getObjects() + self.scene.getPersons():
            collisionInfo = bulcsuBox.collisionWithObject(direction, obj)
            if collisionInfo[CollisionData.COLLISION]:
                objCollision[CollisionData.COLLISION] = True
                objCollision[CollisionData.POSITION] = collisionInfo[CollisionData.POSITION]
        if bulcsuBox.collisionWithSceneBoundaries(direction, self.scene.getBounds()[direction]):
            objCollision[CollisionData.COLLISION] = True
            objCollision[CollisionData.POSITION] = self.scene.getBounds()[direction]
        return objCollision

    def tunnelCheck(self, bulcsuBox):
        found = False
        for tun in self.scene.getTunnels():
            tuncol = bulcsuBox.collisionWithObject(Directions.UP, tun)
            if tuncol[TunnelData.TRANSITION]:
                tunnel = {TunnelData.TRANSITION : True,
                          TunnelData.SCENENAME : tun.getTarget(),
                          TunnelData.DROPOFF : tun.getDropoff(),
                          TunnelData.ORIENTATION : tun.getOrientation()}
                found = True
        if not(found):
            tunnel = {TunnelData.TRANSITION : False}
        return tunnel

    def actionCheck(self, bulcsuBox):
        for currentObject in self.scene.getActionPoints():
            if bulcsuBox.collisionWithObject(Directions.UP, currentObject)[CollisionData.COLLISION]:
                return { "text" : currentObject.getAction(), "pos" : currentObject.getBoundingBox().getVerticalCenter() }
        personAura = 20
        for currentObject in self.scene.getPersons():
            coll = False
            bBox = currentObject.getBoundingBox()
            box = bBox.getBox()
            bBox.updateBox(box.left - personAura, box.top - personAura, box.right + personAura, box.bottom + personAura)
            if bulcsuBox.collisionWithObject(Directions.UP, currentObject)[CollisionData.COLLISION]:
                coll = True
            bBox.updateBox(box.left, box.top, box.right, box.bottom)
            if coll:
                return { "text" : currentObject.getAction(), "pos" : currentObject.getBoundingBox().getVerticalCenter() }
        return {"text" : "noaction", "pos" : 0 }

    def collisions(self):
        bulcsuBox = self.bulcsu.getBoundingBox()

        newX = {"type":"", "value":0}
        if self.moveX >= 0:
            collision = self.collisionCheck(Directions.RIGHT, bulcsuBox)
            if not(collision[CollisionData.COLLISION]):
                newX["type"] = "add"
        elif self.moveX <= 0:
            collision = self.collisionCheck(Directions.LEFT, bulcsuBox)
            if not(collision[CollisionData.COLLISION]):
                newX["type"] = "add"

        newY = {"type":"", "value":0}
        if self.moveY >= 0:
            collision = self.collisionCheck(Directions.DOWN, bulcsuBox)
            if not(collision[CollisionData.COLLISION]):
                newY["type"] = "add"
        elif self.moveY <= 0:
            collision = self.collisionCheck(Directions.UP, bulcsuBox)
            if not(collision[CollisionData.COLLISION]):
                newY["type"] = "add"

        if newX["type"] == "add":
            self.bulcsu.addToPos(Axis.X, self.moveX)
        if newY["type"] == "add":
            self.bulcsu.addToPos(Axis.Y, self.moveY)

    def action(self):
        directions = [Directions.UP, Directions.DOWN,
                      Directions.LEFT, Directions.RIGHT]
        for direction in directions:
            if(self.arrowButtons[direction] != 0):
                self.bulcsu.stop(direction)
                self.arrowButtons[direction] = 0
                pass
        if self.mode == RpgModes.WANDER:
            bulcsuBox = self.bulcsu.getBoundingBox()
            action = self.actionCheck(bulcsuBox)
            if action["text"] != "noaction":
                act = Action.Action().getAction(action["text"])
                if act["type"] == "conversation":
                    self.mode = RpgModes.TALK
                    self.moveX = 0
                    self.moveY = 0
                    self.talk.startConversation(act["id"], self.language, bulcsuBox.getVerticalCenter(), action["pos"])
                return
        if self.mode == RpgModes.TALK:
            if self.talk.action() == False:
                self.mode = RpgModes.WANDER
        return

