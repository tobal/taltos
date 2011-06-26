import pygame.image

class Scene(object):

    def __init__(self, name, image, bounds, tram):
        self.image = image
        self.bounds = {"up" : bounds[0],
                                    "down" : bounds[1],
                                    "left" : bounds[2],
                                    "right" : bounds[3]}
        self.background = pygame.image.load(image).convert()
        self.tram = tram
        self.objects = []
        self.persons = []
        self.actionpoints = []
        self.tunnels = []
        self.name = name

    def is_there_tram(self):
        return self.tram

    def add_object(self, object):
        self.objects.append(object)

    def add_actionpoint(self, object):
        self.actionpoints.append(object)

    def add_person(self, object):
        self.persons.append(object)

    def add_tunnel(self, object):
        self.tunnels.append(object)

    def get_objects(self):
        return self.objects

    def get_persons(self):
        return self.persons

    def get_actionpoints(self):
        return self.actionpoints

    def get_tunnels(self):
        return self.tunnels

    def get_background(self):
        return self.background

    def get_bounds(self):
        return self.bounds

    def get_name(self):
        return self.name

    def draw_background(self, screen):
        screen.blit(self.background, (0,0))

    # order can be "front" or "back"
    def draw_objects(self, order, sprite_pos_y, screen):
        if order == "front":
            for obj in self.objects:
                if sprite_pos_y < obj.get_bounding_box().get_center():
                    screen.blit(obj.get_image(), (obj.get_pos()))
            for obj in self.persons:
                if sprite_pos_y < obj.get_bounding_box().get_center():
                    screen.blit(obj.get_image(), (obj.get_pos()))
        if order == "back":
            for obj in self.objects:
                if sprite_pos_y >= obj.get_bounding_box().get_center():
                    screen.blit(obj.get_image(), (obj.get_pos()))
            for obj in self.persons:
                if sprite_pos_y >= obj.get_bounding_box().get_center():
                    screen.blit(obj.get_image(), (obj.get_pos()))
        return
