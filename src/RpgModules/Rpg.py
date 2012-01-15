
from RpgModules import Sprite
from RpgModules import SceneBuilder
from RpgModules import RpgTalker
from RpgModules import Action
from RpgModules import Tram
from CommonModules.GameModule import GameModule
from CommonModules.Constants import RpgModes
from CommonModules.Constants import RpgScenes
from CommonModules.Constants import Directions
from CommonModules.Constants import TunnelData
from CommonModules.Constants import CollisionData
from CommonModules.Constants import DrawingOrder
from CommonModules.Constants import Axis

class Rpg(GameModule):

    def __init__(self, gameScreen, language):
        GameModule.__init__(self, gameScreen, language)

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

    def leftKeyUp(self):
        if self.mode == RpgModes.TALK:
            pass
        if self.mode == RpgModes.WANDER:
            self.arrowButtons[Directions.LEFT] = 2
            self.moveSprite()

    def rightKeyUp(self):
        if self.mode == RpgModes.TALK:
            pass
        if self.mode == RpgModes.WANDER:
            self.arrowButtons[Directions.RIGHT] = 2
            self.moveSprite()

    def upKeyUp(self):
        if self.mode == RpgModes.TALK:
            pass
        if self.mode == RpgModes.WANDER:
            self.arrowButtons[Directions.UP] = 2
            self.moveSprite()

    def downKeyUp(self):
        if self.mode == RpgModes.TALK:
            pass
        if self.mode == RpgModes.WANDER:
            self.arrowButtons[Directions.DOWN] = 2
            self.moveSprite()

    def leftKeyDown(self):
        if self.mode == RpgModes.TALK:
            pass
        if self.mode == RpgModes.WANDER:
            self.arrowButtons[Directions.LEFT] = 1
            self.moveSprite()

    def rightKeyDown(self):
        if self.mode == RpgModes.TALK:
            pass
        if self.mode == RpgModes.WANDER:
            self.arrowButtons[Directions.RIGHT] = 1
            self.moveSprite()

    def upKeyDown(self):
        if self.mode == RpgModes.TALK:
            self.talk.arrowUp()
        if self.mode == RpgModes.WANDER:
            self.arrowButtons[Directions.UP] = 1
            self.moveSprite()

    def downKeyDown(self):
        if self.mode == RpgModes.TALK:
            self.talk.arrowDown()
        if self.mode == RpgModes.WANDER:
            self.arrowButtons[Directions.DOWN] = 1
            self.moveSprite()

    def enter(self):
        self.action()

    def postAction(self):
        self.moveSprite()

    def moveSprite(self):
        moveSpeed = 5.5
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

