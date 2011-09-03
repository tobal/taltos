
import pygame
from pygame.locals import *
import random

from Rpg import Sprite
from Rpg import Scene
from Rpg import SceneBuilder
import MainExceptions
from Rpg.Objects import BoundingBox
from Rpg import RPGTalker
from Rpg import Actions

class Tram(object):

    def __init__(self):
        self.timer = 0
        self.drawing = False
        self.speed = 20.0
        self.altitude = 10
        self.pos = -2846.0
        self.min_time = 400
        self.max_time = 1000
        self.due = random.randint(self.min_time, self.max_time)
        self.villamos = pygame.image.load("../resrc/img/RPG/villamos.png").convert_alpha()
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
                self.due = random.randint(self.min_time, self.max_time)
        return

    def draw(self, screen):
        if self.drawing:
            screen.blit(self.villamos, (self.pos, self.altitude))
        return

    def modify_pos(self, value):
        self.pos += value
        return

class RPGModule(object):

    def __init__(self, screen, resolution, language):
        self.screen = screen
        self.resolution = resolution
        self.make_scene()
        self.make_sprite()
        self.talk = RPGTalker.RPGTalker()
        self.move_x, self.move_y =0, 0
        self.anim = 0
        if self.scene.is_there_tram():
            self.villamos = Tram()
        self.mode = "wander"         # can be "wander" or "talk" (python needs enum type)
        self.lang = language
        self.arrowbuttons = {"up" : 0,
                             "down" : 0,
                             "left" : 0,
                             "right" : 0,
                             "prevup" : 0,
                             "prevdown" : 0,
                             "prevleft" : 0,
                             "prevright" : 0,}

    def game_loop(self):
        self.event_handler()
        if self.mode == "wander":
            self.animation()
        tunnel = self.tunnel_check(self.bulcsu.get_bounding_box())
        if tunnel["bool"]:
            self.change_scene(tunnel["scenename"], tunnel["dropoff"])
        self.collisions()
        if self.scene.is_there_tram():
            self.villamos.loop()

        # drawing the whole scene
        self.scene.draw_background(self.screen)
        self.scene.draw_objects("back", self.bulcsu.get_bounding_box().get_center(), self.screen)
        self.screen.blit(self.bulcsu.get_actual_sprite(), (self.bulcsu.get_pos_x(), self.bulcsu.get_pos_y()))
        self.scene.draw_objects("front", self.bulcsu.get_bounding_box().get_center(), self.screen)
        if self.scene.is_there_tram():
            self.villamos.draw(self.screen)
        if self.mode == "talk":
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

    def make_scene(self):
        # making scene instances
        self.scenes = {"hardware" : SceneBuilder.build_scene("hardware"),
                       "street" : SceneBuilder.build_scene("street"),
                       "shop" : SceneBuilder.build_scene("shop")}
        self.scene = self.scenes["hardware"]
        self.scene_bounds = self.scene.get_bounds()

    def change_scene(self, scenename, dropoff_point):
        self.scene = self.scenes[scenename]
        self.bulcsu.set_pos(dropoff_point)
        # FIXME: should not have a redundant scene bounds value in this class
        self.scene_bounds = self.scene.get_bounds()
        # here is a very temporary and very disgusting solution to the tram-problem
        if self.scene.is_there_tram():
            if scenename == "street":
                value = -1024
            elif scenename == "hardware":
                value = 1024
            self.villamos.modify_pos(value)

    def make_sprite(self):
        # making sprite instance
        self.bulcsu = Sprite.ProtagonistSprite(80, 340)

    def event_handler(self):
        if self.mode == "wander":
            move_speed = 4.0

            for event in pygame.event.get():
                if event.type == QUIT:
                    raise MainExceptions.Exit()
                if event.type == KEYDOWN:
                    if (event.key == K_a) or (event.key == K_LEFT):
                        self.arrowbuttons["left"] = 1
                    if (event.key == K_d) or (event.key == K_RIGHT):
                        self.arrowbuttons["right"] = 1
                    if (event.key == K_w) or (event.key == K_UP):
                        self.arrowbuttons["up"] = 1
                    if (event.key == K_s) or (event.key == K_DOWN):
                        self.arrowbuttons["down"] = 1
                    if (event.key == K_q) or (event.key == K_ESCAPE):
                        raise MainExceptions.Exit()
                    if (event.key == K_e) or (event.key == K_RETURN):
                        self.action()
                if event.type == KEYUP:
                    if (event.key == K_a) or (event.key == K_LEFT):
                        self.arrowbuttons["left"] = 2
                    if (event.key == K_d) or (event.key == K_RIGHT):
                        self.arrowbuttons["right"] = 2
                    if (event.key == K_w) or (event.key == K_UP):
                        self.arrowbuttons["up"] = 2
                    if (event.key == K_s) or (event.key == K_DOWN):
                        self.arrowbuttons["down"] = 2

            if self.arrowbuttons["left"] == 1:
                if self.move_x == 0:
                    self.move_x = -move_speed
                    self.bulcsu.go_left()
            if self.arrowbuttons["right"] == 1:
                if self.move_x == 0:
                    self.move_x = move_speed
                    self.bulcsu.go_right()
            if self.arrowbuttons["up"] == 1:
                if self.move_y == 0:
                    self.move_y = -move_speed
                    if self.move_x == 0:
                        self.bulcsu.go_up()
            if self.arrowbuttons["down"] == 1:
                if self.move_y == 0:
                    self.move_y = move_speed
                    if self.move_x == 0:
                        self.bulcsu.go_down()
            if self.arrowbuttons["left"] == 2:
                if self.move_x < 0:
                    self.move_x = 0
                    self.bulcsu.stop_left()
                self.arrowbuttons["left"] == 0
            if self.arrowbuttons["right"] == 2:
                if self.move_x > 0:
                    self.move_x = 0
                    self.bulcsu.stop_right()
                self.arrowbuttons["right"] == 0
            if self.arrowbuttons["up"] == 2:
                if self.move_y < 0:
                    self.move_y = 0
                    if self.move_x == 0:
                        self.bulcsu.stop_up()
                self.arrowbuttons["up"] == 0
            if self.arrowbuttons["down"] == 2:
                if self.move_y > 0:
                    self.move_y = 0
                    if self.move_x == 0:
                        self.bulcsu.stop_down()
                self.arrowbuttons["down"] == 0

        if self.mode == "talk":
            for event in pygame.event.get():
                if event.type == QUIT:
                    raise MainExceptions.Exit()
                if event.type == KEYDOWN:
                    if event.key == K_w or event.key == K_UP:
                        self.talk.arrow_up()
                    if event.key == K_s or event.key == K_DOWN:
                        self.talk.arrow_down()
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
        anim_speed = 6
        animated = False

        if self.move_x > 0:
            self.anim += 1
            animated = True
            if self.anim > anim_speed:
                self.bulcsu.go_right()
                self.anim = 0
        elif self.move_x < 0:
            self.anim += 1
            animated = True
            if self.anim > anim_speed:
                self.bulcsu.go_left()
                self.anim = 0

        if self.move_y > 0:
            if not animated:
                self.anim += 1
            if self.anim > anim_speed:
                if self.move_x == 0:
                    self.bulcsu.go_down()
                self.anim = 0
        elif self.move_y < 0:
            if not animated:
                self.anim += 1
            if self.anim > anim_speed:
                if self.move_x == 0:
                    self.bulcsu.go_up()
                self.anim = 0

    def collision_check(self, direction, bulcsuBox):
        obj_collision = {"bool" : False,
                         "pos" : 0}
        for obj in self.scene.get_objects() + self.scene.get_persons():
            collision_info = bulcsuBox.collision_with_object(direction, obj)
            if collision_info["bool"]:
                obj_collision["bool"] = True
                obj_collision["pos"] = collision_info["pos"]
        if bulcsuBox.collision_with_scene_boundaries(direction, self.scene_bounds[direction]):
            obj_collision["bool"] = True
            obj_collision["pos"] = self.scene_bounds[direction]
        return obj_collision

    def tunnel_check(self, bulcsuBox):
        notfound = True
        for tun in self.scene.get_tunnels():
            tuncol = bulcsuBox.collision_with_object("up", tun)
            if tuncol["bool"]:
                tunnel = {"bool" : True,
                          "scenename" : tun.get_target(),
                          "dropoff" : tun.get_dropoff(),
                          "orientation" : tun.get_orientation()}
                notfound = False
        if notfound:
            tunnel = {"bool" : False}
        return tunnel

    def action_check(self, bulcsuBox):
        for obj in self.scene.get_actionpoints():
            if bulcsuBox.collision_with_object("up", obj)["bool"]:
                return { "text" : obj.get_action(), "pos" : obj.get_bounding_box().get_vert_center() }
        person_aura = 20
        for obj in self.scene.get_persons():
            coll = False
            bbox = obj.get_bounding_box()
            box = bbox.get_box()
            bbox.update_box(box["x1"] - person_aura, box["y1"] - person_aura, box["x2"] + person_aura, box["y2"] + person_aura)
            if bulcsuBox.collision_with_object("up", obj)["bool"]:
                coll = True
            bbox.update_box(box["x1"], box["y1"], box["x2"], box["y2"])
            if coll:
                return { "text" : obj.get_action(), "pos" : obj.get_bounding_box().get_vert_center() }
        return {"text" : "noaction", "pos" : 0 }

    def collisions(self):
        bulcsuBox = self.bulcsu.get_bounding_box()

        new_x = {"type":"", "value":0}
        if self.move_x >= 0:
            collision = self.collision_check("right", bulcsuBox)
            if not(collision["bool"]):
                new_x["type"] = "add"
        elif self.move_x <= 0:
            collision = self.collision_check("left", bulcsuBox)
            if not(collision["bool"]):
                new_x["type"] = "add"

        new_y = {"type":"", "value":0}
        if self.move_y >= 0:
            collision = self.collision_check("down", bulcsuBox)
            if not(collision["bool"]):
                new_y["type"] = "add"
        elif self.move_y <= 0:
            collision = self.collision_check("up", bulcsuBox)
            if not(collision["bool"]):
                new_y["type"] = "add"

        if new_y["type"] == "add":
            self.bulcsu.add_to_pos("y", self.move_y)
        if new_x["type"] == "add":
            self.bulcsu.add_to_pos("x", self.move_x)


    def action(self):
        if self.mode == "wander":
            bulcsuBox = self.bulcsu.get_bounding_box()
            action = self.action_check(bulcsuBox)
            if action["text"] != "noaction":
                act = Actions.get_action(action["text"])
                if act["type"] == "conversation":
                    self.mode = "talk"
                    self.move_x = 0
                    self.move_y = 0
                    self.talk.start_conversation(act["id"], self.lang, bulcsuBox.get_vert_center(), action["pos"])
                return
        if self.mode == "talk":
            if self.talk.action() == False:
                self.mode = "wander"
        return

