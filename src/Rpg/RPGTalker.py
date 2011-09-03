import pygame

import Conversations

class RPGTalker:

# TODO: The whole conversation module needs a major rewrite
# TODO: Get texts from a PO file

    # RPGTalker acts like a state machine
    def __init__(self):
        self.actual_branch = 1
        self.end = False
        self.drawing = False
        self.gorr = pygame.font.Font("../resrc/fonts/gorrisans.ttf", 18)
        self.rov = pygame.font.Font("../resrc/fonts/rovmajb.ttf", 32)
        return

    def action(self):
        if self.end:
            self.drawing = False
            self.end = False
            self.actual_branch = 1
            return False
        else:
            if self.isthereanswer:
                self.actual_branch = self.str["answers"][self.actual_answer][1]

            self.str = self.conv.get_next_string(self.actual_branch)
            if self.str["end"]:
                self.end = True
            self.draw_text = self.str["text"]
            if self.str["answers"] != []:
                self.draw_answers = self.str["answers"]
                self.isthereanswer = True
                self.actual_answer = 0
            else:
                self.isthereanswer = False
            if self.str["whosaid"]:
                self.draw_talk_pos = self.char_pos
            else:
                self.draw_talk_pos = self.obj_pos
            self.update_textsurfaces()
            self.update_polygon()
            return True
        return

    def start_conversation(self, conv, lang, char_pos, obj_pos):
        self.conv = Conversations.Conversations(conv, lang)
        self.drawing = True
        self.char_pos = char_pos
        self.obj_pos = obj_pos
        # defining state variables
        self.draw_text = ""
        self.isthereanswer = False
        self.draw_answers = []
        self.draw_talk_pos = 0.0
        self.poly_points = []
        self.actual_answer = 0
        self.str = {}
        self.txtsrf = []
        if lang == "rov":
            self.font = self.rov
        else:
            self.font = self.gorr
        self.action()
        return

    def update_polygon(self):
        self.poly_points = []
        self.offset = 0
        if self.draw_talk_pos > 640:
            self.offset = self.draw_talk_pos - 640
            self.offset = -self.offset
        if self.draw_talk_pos < 380:
            self.offset = 380 - self.draw_talk_pos
        self.poly_points.append((self.draw_talk_pos,315))
        self.poly_points.append((self.draw_talk_pos,250))
        self.poly_points.append((self.draw_talk_pos-260+self.offset,250))
        self.poly_points.append((self.draw_talk_pos-320+self.offset,190))
        self.poly_points.append((self.draw_talk_pos-320+self.offset,60))
        self.poly_points.append((self.draw_talk_pos-260+self.offset,0))
        self.poly_points.append((self.draw_talk_pos+320+self.offset,0))
        self.poly_points.append((self.draw_talk_pos+380+self.offset,60))
        self.poly_points.append((self.draw_talk_pos+380+self.offset,190))
        self.poly_points.append((self.draw_talk_pos+320+self.offset,250))
        self.poly_points.append((self.draw_talk_pos+50,250))
        self.poly_points.append((self.draw_talk_pos,315))
        return

    def update_textsurfaces(self):
        self.txtsrf = []
        if self.isthereanswer:
            for i in range(self.draw_answers.__len__()):
                if self.actual_answer == i:
                    self.txtsrf.append(self.font.render(self.draw_answers[i][0], True, (255,255,255), (100,100,100)))
                else:
                    self.txtsrf.append(self.font.render(self.draw_answers[i][0], True, (100,100,100)))
        else:
            count = 0
            secondcount = 0
            borders = [0]
            texts = []
            for char in self.draw_text:
                if char == " ":
                    if secondcount >= 50:
                        secondcount = -1
                        borders.append(count)
                count += 1
                secondcount += 1
            len = borders.__len__()
            csojj = range(borders.__len__())
            if borders.__len__() == 1:
                texts.append(self.draw_text[borders[0]:])
            else:
                for i in range(borders.__len__()-1):
                    texts.append(self.draw_text[borders[i]:borders[i+1]])
                texts.append(self.draw_text[borders[-1]:])
            for txt in texts:
                srf = self.font.render(txt, True, (100,100,100))
                self.txtsrf.append(srf)

    def arrow_down(self):
        if self.isthereanswer:
            if self.actual_answer < self.draw_answers.__len__()-1:
                self.actual_answer += 1
            else:
                self.actual_answer = 0
        self.update_textsurfaces()

    def arrow_up(self):
        if self.isthereanswer:
            if self.actual_answer > 0:
                self.actual_answer -= 1
            else:
                self.actual_answer = self.draw_answers.__len__()-1
        self.update_textsurfaces()

    # drawing is done based on the state variables
    def draw(self, screen):
        if self.drawing:
            pygame.draw.polygon(screen, (255,255,255), self.poly_points)
            pygame.draw.polygon(screen, (100,100,100), self.poly_points, 5)
            row = 50
            for textsurface in self.txtsrf:
                screen.blit(textsurface, (self.draw_talk_pos-280+self.offset, row))
                row += 30
        return