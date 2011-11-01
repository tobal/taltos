
import pygame
from pygame.locals import *
import random

from Rpg import Sprite
from Rpg import SceneBuilder
import MainExceptions
from Rpg import RPGTalker
from Rpg import Actions
from src.CommonModules.Images import RpgImages
from src.CommonModules.Constants import RpgModes
from src.CommonModules.Constants import RpgScenes
from src.CommonModules.Constants import Directions
from src.CommonModules.Constants import TunnelData
from src.CommonModules.Constants import CollisionData
from src.CommonModules.Constants import DrawingOrder

class Tram(object):

    def __init__(self):
        self.timer = 0
        self.drawing = False
        self.speed = 20.0
        self.altitude = 10
        self.pos = -2846.0
        self.minTime = 400
        self.maxTime = 1000
        self.due = random.randint(self.minTime, self.maxTime)
        self.villamos = pygame.image.load(RpgImages.RpgImages.TRAM).convert_alpha()
        return

    def loop(self):
        if not(self.drawing):
            self.timer += 1
            if self.timer > self.due:
                self.pos = -2846.0
                self.drawing = True
        else:
            self.pos += self.speed
            if self.pos >= 1024:
                self.drawing = False
                self.timer = 0
                self.due = random.randint(self.minTime, self.maxTime)
        return

    def draw(self, screen):
        if self.drawing:
            screen.blit(self.villamos, (self.pos, self.altitude))
        return

    def modifyPos(self, value):
        self.pos += value
        return

class RPGModule(object):

    def __init__(self, screen, resolution, language):
        self.screen = screen
        self.resolution = resolution
        self.makeScene()
        self.makeSprite()
        self.talk = RPGTalker.RPGTalker()
        self.moveX, self.moveY = 0, 0
        self.anim = 0
        if self.scene.isThereTram():
            self.villamos = Tram()
        self.mode = RpgModes.WANDER
        self.lang = language
        self.arrowButtons = {Directions.UP : 0,
                             Directions.DOWN : 0,
                             Directions.LEFT : 0,
                             Directions.RIGHT : 0}
        self.prevArrowButtons = {Directions.UP : 0,
                                 Directions.DOWN : 0,
                                 Directions.LEFT : 0,
                                 Directions.RIGHT: 0,}

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
        self.scene.drawObjects(DrawingOrder.BACK, self.bulcsu.getBoundingBox().getCenter(), self.screen)
        self.screen.blit(self.bulcsu.getCurrentSprite(), (self.bulcsu.getPosX(), self.bulcsu.getPosY()))
        self.scene.drawObjects(DrawingOrder.FRONT, self.bulcsu.getBoundingBox().getCenter(), self.screen)
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
        self.sceneBounds = self.scene.getBounds()

    def changeScene(self, scene, dropoffPoint):
        self.scene = self.scenes[scene]
        self.bulcsu.setPos(dropoffPoint)
        # FIXME: should not have a redundant scene bounds value in this class
        self.sceneBounds = self.scene.getBounds()
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
            moveSpeed = 4.0

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
                    self.bulcsu.goLeft()
            if self.arrowButtons[Directions.RIGHT] == 1:
                if self.moveX == 0:
                    self.moveX = moveSpeed
                    self.bulcsu.goRight()
            if self.arrowButtons[Directions.UP] == 1:
                if self.moveY == 0:
                    self.moveY = -moveSpeed
                    if self.moveX == 0:
                        self.bulcsu.goUp()
            if self.arrowButtons[Directions.DOWN] == 1:
                if self.moveY == 0:
                    self.moveY = moveSpeed
                    if self.moveX == 0:
                        self.bulcsu.goDown()
            if self.arrowButtons[Directions.LEFT] == 2:
                if self.moveX < 0:
                    self.moveX = 0
                    self.bulcsu.stopLeft()
                self.arrowButtons[Directions.LEFT] == 0
            if self.arrowButtons[Directions.RIGHT] == 2:
                if self.moveX > 0:
                    self.moveX = 0
                    self.bulcsu.stopRight()
                self.arrowButtons[Directions.RIGHT] == 0
            if self.arrowButtons[Directions.UP] == 2:
                if self.moveY < 0:
                    self.moveY = 0
                    if self.moveX == 0:
                        self.bulcsu.stopUp()
                self.arrowButtons[Directions.UP] == 0
            if self.arrowButtons[Directions.DOWN] == 2:
                if self.moveY > 0:
                    self.moveY = 0
                    if self.moveX == 0:
                        self.bulcsu.stopDown()
                self.arrowButtons[Directions.DOWN] == 0

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
                self.bulcsu.goRight()
                self.anim = 0
        elif self.moveX < 0:
            self.anim += 1
            animated = True
            if self.anim > animSpeed:
                self.bulcsu.goLeft()
                self.anim = 0

        if self.moveY > 0:
            if not animated:
                self.anim += 1
            if self.anim > animSpeed:
                if self.moveX == 0:
                    self.bulcsu.goDown()
                self.anim = 0
        elif self.moveY < 0:
            if not animated:
                self.anim += 1
            if self.anim > animSpeed:
                if self.moveX == 0:
                    self.bulcsu.goUp()
                self.anim = 0

    def collisionCheck(self, direction, bulcsuBox):
        objCollision = {CollisionData.COLLISION : False,
                        CollisionData.POSITION : 0}
        for obj in self.scene.getObjects() + self.scene.getPersons():
            collisionInfo = bulcsuBox.collisionWithObject(direction, obj)
            if collisionInfo[CollisionData.COLLISION]:
                objCollision[CollisionData.COLLISION] = True
                objCollision[CollisionData.POSITION] = collisionInfo[CollisionData.POSITION]
        if bulcsuBox.collisionWithSceneBoundaries(direction, self.sceneBounds[direction]):
            objCollision[CollisionData.COLLISION] = True
            objCollision[CollisionData.POSITION] = self.sceneBounds[direction]
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
        for obj in self.scene.getActionPoints():
            if bulcsuBox.collisionWithObject(Directions.UP, obj)[CollisionData.COLLISION]:
                return { "text" : obj.getAction(), "pos" : obj.getBoundingBox().getVertCenter() }
        personAura = 20
        for obj in self.scene.getPersons():
            coll = False
            bBox = obj.getBoundingBox()
            box = bBox.getBox()
            bBox.updateBox(box["x1"] - personAura, box["y1"] - personAura, box["x2"] + personAura, box["y2"] + personAura)
            if bulcsuBox.collisionWithObject("up", obj)[CollisionData.COLLISION]:
                coll = True
            bBox.updateBox(box["x1"], box["y1"], box["x2"], box["y2"])
            if coll:
                return { "text" : obj.getAction(), "pos" : obj.getBoundingBox().getVertCenter() }
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

        if newY["type"] == "add":
            self.bulcsu.addToPos("y", self.moveY)
        if newX["type"] == "add":
            self.bulcsu.addToPos("x", self.moveX)


    def action(self):
        if self.mode == RpgModes.WANDER:
            bulcsuBox = self.bulcsu.getBoundingBox()
            action = self.actionCheck(bulcsuBox)
            if action["text"] != "noaction":
                act = Actions.getAction(action["text"])
                if act["type"] == "conversation":
                    self.mode = "talk"
                    self.moveX = 0
                    self.moveY = 0
                    self.talk.startConversation(act["id"], self.lang, bulcsuBox.getVertCenter(), action["pos"])
                return
        if self.mode == RpgModes.TALK:
            if self.talk.action() == False:
                self.mode = RpgModes.WANDER
        return

