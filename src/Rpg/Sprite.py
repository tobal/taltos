import pygame
from pygame.locals import *
from Objects import BoundingBox

class ProtagonistSprite(object):

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.load_sprites()
        self.bBox = BoundingBox(self.pos_x, self.pos_y + 200, self.pos_x + 81, self.pos_y + 232)
        return

    def load_img(self,  imgname,  alpha):
        img_str = "../resrc/img/RPG/" + imgname + ".png"
        if alpha:
            img = pygame.image.load(img_str).convert_alpha()
        else:
            img = pygame.image.load(img_str).convert()
        return img

    def load_sprites(self):
        lRightstand = [ self.load_img("jobbraall",  True) ]
        lRightwalk = []
        for x in range(1, 7):
            lRightwalk.append(self.load_img("jobbralep" + str(x),  True))

        lLeftstand = [ self.load_img("balraall", True) ]
        lLeftwalk = []
        for x in range(1, 7):
            lLeftwalk.append(self.load_img("balralep" + str(x), True))

        lBackstand = [ self.load_img("hattalall",  True) ]
        lBackwalk = [ self.load_img("hattallep1",  True),
                            self.load_img("hattalall",  True),
                            self.load_img("hattallep2",  True),
                            self.load_img("hattalall",  True) ]

        lFrontstand = [ self.load_img("szembenall",  True) ]
        lFrontwalk = [ self.load_img("szembenlep1",  True),
                            self.load_img("szembenlep2",  True),
                            self.load_img("szembenlep3",  True),
                            self.load_img("szembenlep2",  True) ]

        self.sprite = {"rightstand" : lRightstand,
                                "rightwalk" : lRightwalk,
                                "leftstand" : lLeftstand,
                                "leftwalk" : lLeftwalk,
                                "backstand" : lBackstand,
                                "backwalk" : lBackwalk,
                                "frontstand" : lFrontstand,
                                "frontwalk" : lFrontwalk}

        self.actual_sprite = self.sprite["rightstand"][0]

    def get_actual_sprite(self):
        return self.actual_sprite

    def going(self, str, spritenum):
        if self.actual_sprite in self.sprite[str]:
            if self.sprite[str].index(self.actual_sprite) >= spritenum-1:
                self.actual_sprite = self.sprite[str][0]
            else:
                self.actual_sprite = self.sprite[str][self.sprite[str].index(self.actual_sprite)+1]
        else:
            self.actual_sprite = self.sprite[str][0]

    def go_right(self):
        self.going("rightwalk", 6)
        return

    def go_left(self):
        self.going("leftwalk", 6)
        return

    def go_up(self):
        self.going("backwalk", 4)
        return

    def go_down(self):
        self.going("frontwalk", 4)
        return

    def stop_right(self):
        self.actual_sprite = self.sprite["rightstand"][0]

    def stop_left(self):
        self.actual_sprite = self.sprite["leftstand"][0]

    def stop_up(self):
        self.actual_sprite = self.sprite["backstand"][0]

    def stop_down(self):
        self.actual_sprite = self.sprite["frontstand"][0]

    # axis has to be x or y
    def add_to_pos(self, axis, move):
        if axis == "x":
            self.pos_x += move
        elif axis == "y":
            self.pos_y += move

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_bounding_box(self):
        self.bBox.update_box(self.pos_x, self.pos_y + 200, self.pos_x + 81, self.pos_y + 232)
        return self.bBox

    def set_pos_x(self, x):
        self.pos_x = x

    def set_pos_y(self, y):
        self.pos_y = y

    def set_pos(self, point):
        self.pos_x = point[0]
        self.pos_y = point[1]
