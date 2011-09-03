import pygame.image

class BoundingBox(object):

    def __init__(self, x1, y1, x2, y2):
        # why didn't I just use Rect class??! shoot me plz
        self.box = {"x1" : x1, "x2" : x2, "y1" : y1, "y2" : y2}
        return

    def update_box(self, x1, y1, x2, y2):
        self.box = {"x1" : x1, "x2" : x2, "y1" : y1, "y2" : y2}

    def get_center(self):
        y1, y2 = self.box["y1"], self.box["y2"]
        return y1+((y2-y1)/2)

    def get_vert_center(self):
        x1, x2 = self.box["x1"], self.box["x2"]
        return x1+((x2-x1)/2)

    def get_box(self):
        return self.box

    def collision_with_object(self, direction, obj):
        obj_box = obj.get_bounding_box().get_box()
        return_value = {"bool" : False,
                        "pos" : 0}

        # I want to punch myself in the face for writing this code...
        if      (  (self.box["x1"]+5 < obj_box["x1"] and self.box["x2"]-5 > obj_box["x1"])
                    or
                    (self.box["x1"]+5 < obj_box["x2"] and self.box["x2"]-5 > obj_box["x2"])
                    or
                    (
                        (self.box["x1"]+5 > obj_box["x1"] and self.box["x2"]-5 > obj_box["x1"])
                        and
                        (self.box["x1"]+5 < obj_box["x2"] and self.box["x2"]-5 < obj_box["x2"])
                    )):
            if direction == "up":
                if (self.box["y1"] <= obj_box["y2"]) and (self.box["y2"]-5 > obj_box["y1"]) :
                    return_value["bool"] = True
                    return_value["pos"] = obj_box["y2"]
                else:
                    return_value["bool"] = False
            if direction == "down":
                if (self.box["y2"] >= obj_box["y1"]) and (self.box["y1"]+5 < obj_box["y2"]):
                    return_value["bool"] = True
                    return_value["pos"] = obj_box["y1"]
                else:
                    return_value["bool"] = False

        if      (  (self.box["y1"]+5 < obj_box["y1"] and self.box["y2"]-5 > obj_box["y1"])
                    or
                    (self.box["y1"]+5 < obj_box["y2"] and self.box["y2"]-5 > obj_box["y2"])
                    or
                    (
                        (self.box["y1"]+5 > obj_box["y1"] and self.box["y2"]-5 > obj_box["y1"])
                        and
                        (self.box["y1"]+5 < obj_box["y2"] and self.box["y2"]-5 < obj_box["y2"])
                    )):
            if direction == "left":
                if (self.box["x1"] <= obj_box["x2"]) and (self.box["x2"]-5 > obj_box["x1"]):
                    return_value["bool"] = True
                    return_value["pos"] = obj_box["x2"]
                else:
                    return_value["bool"] = False
            if direction == "right":
                if (self.box["x2"] >= obj_box["x1"]) and (self.box["x1"]+5 < obj_box["x2"]):
                    return_value["bool"] = True
                    return_value["pos"] = obj_box["x1"]
                else:
                    return_value["bool"] = False
        return return_value

    # direction can only be "up", "down", "left" or "right"
    def collision_with_scene_boundaries(self, direction, bound):
        if direction == "up":
            if self.box["y1"] <= bound:
                return True
            else:
                return False
        if direction == "down":
            if self.box["y2"] >= bound:
                return True
            else:
                return False
        if direction == "left":
            if self.box["x1"] <= bound:
                return True
            else:
                return False
        if direction == "right":
            if self.box["x2"] >= bound:
                return True
            else:
                return False
        return

class Object(object):

    def __init__(self, x, y, dim_x, dim_y):
        self.pos = [x, y]
        self.dimensions = [dim_x, dim_y]
        self.bBox = BoundingBox(x, y, x + dim_x, y + dim_y)
        return

    def get_pos(self):
        return self.pos

    def get_dimensions(self):
        return self.dimensions

    def get_bounding_box(self):
        return self.bBox

class ActionMark(Object):

    def __init__(self, x, y, dim_x, dim_y, action):
        Object.__init__(self, x, y, dim_x, dim_y)
        self.action = action
        return

    def get_action(self):
        return self.action

class TunnelObject(Object):

    def __init__(self, x, y, dim_x, dim_y, target, dropoff_point, orient):
        Object.__init__(self, x, y, dim_x, dim_y)
        self.target = target
        self.dropoff = dropoff_point
        self.orientation = orient # orient can be 0 for horizontal, 1 for vertical or 2 for absolute
        return

    def get_target(self):
        return self.target

    def get_dropoff(self):
        return self.dropoff

    def get_orientation(self):
        return self.orientation

class ObjectSprite(Object):

    def __init__(self, x, y, image, thickness):
        image = "../resrc/img/RPG/" + image + ".png"
        self.image = pygame.image.load(image).convert_alpha()
        dim_x,  dim_y = self.image.get_width(), self.image.get_height()
        Object.__init__(self, x, y, dim_x, dim_y)
        self.thickness = thickness

        self.bBox = BoundingBox(x, y + dim_y - thickness, x + dim_x, y + dim_y)
        return

    def get_image(self):
        return self.image

class Person(ObjectSprite):

    def __init__(self, x, y, image, thickness,  action):
        ObjectSprite.__init__(self, x, y, image, thickness)
        self.action = action
        return

    def get_action(self):
        return self.action
