import pygame

from RpgModules import Conversations

class RpgTalker:

    # RPGTalker acts like a state machine
    def __init__(self):
        self.actualBranch = 1
        self.end = False
        self.drawing = False
        self.gorr = pygame.font.Font("../resrc/fonts/gorrisans.ttf", 18)
        self.rov = pygame.font.Font("../resrc/fonts/rovmajb.ttf", 32)
        return

    def action(self):
        if self.end:
            self.drawing = False
            self.end = False
            self.actualBranch = 1
            return False
        else:
            if self.isThereAnswer:
                self.actualBranch = self.str["answers"][self.actualAnswer][1]

            self.str = self.conv.getNextString(self.actualBranch)
            if self.str["end"]:
                self.end = True
            self.drawText = self.str["text"]
            if self.str["answers"] != []:
                self.drawAnswers = self.str["answers"]
                self.isThereAnswer = True
                self.actualAnswer = 0
            else:
                self.isThereAnswer = False
            if self.str["whosaid"]:
                self.drawTalkPos = self.charPos
            else:
                self.drawTalkPos = self.objPos
            self.updateTextSurfaces()
            self.updatePolygon()
            return True
        return

    def startConversation(self, conv, lang, charPos, objPos):
        self.conv = Conversations.Conversations(conv, lang)
        self.drawing = True
        self.charPos = charPos
        self.objPos = objPos
        # defining state variables
        self.drawText = ""
        self.isThereAnswer = False
        self.drawAnswers = []
        self.drawTalkPos = 0.0
        self.polyPoints = []
        self.actualAnswer = 0
        self.str = {}
        self.textSurfaces = []
        if lang == "rov":
            self.font = self.rov
        else:
            self.font = self.gorr
        self.action()
        return

    def updatePolygon(self):
        self.polyPoints = []
        self.offset = 0
        if self.drawTalkPos > 640:
            self.offset = self.drawTalkPos - 640
            self.offset = -self.offset
        if self.drawTalkPos < 380:
            self.offset = 380 - self.drawTalkPos
        self.polyPoints.append((self.drawTalkPos,315))
        self.polyPoints.append((self.drawTalkPos,250))
        self.polyPoints.append((self.drawTalkPos-260+self.offset,250))
        self.polyPoints.append((self.drawTalkPos-320+self.offset,190))
        self.polyPoints.append((self.drawTalkPos-320+self.offset,60))
        self.polyPoints.append((self.drawTalkPos-260+self.offset,0))
        self.polyPoints.append((self.drawTalkPos+320+self.offset,0))
        self.polyPoints.append((self.drawTalkPos+380+self.offset,60))
        self.polyPoints.append((self.drawTalkPos+380+self.offset,190))
        self.polyPoints.append((self.drawTalkPos+320+self.offset,250))
        self.polyPoints.append((self.drawTalkPos+50,250))
        self.polyPoints.append((self.drawTalkPos,315))
        return

    def updateTextSurfaces(self):
        self.textSurfaces = []
        if self.isThereAnswer:
            for i in range(self.drawAnswers.__len__()):
                if self.actualAnswer == i:
                    self.textSurfaces.append(self.font.render(self.drawAnswers[i][0], True, (255,255,255), (100,100,100)))
                else:
                    self.textSurfaces.append(self.font.render(self.drawAnswers[i][0], True, (100,100,100)))
        else:
            count = 0
            secondCount = 0
            borders = [0]
            texts = []
            for char in self.drawText:
                if char == " ":
                    if secondCount >= 50:
                        secondCount = -1
                        borders.append(count)
                count += 1
                secondCount += 1
            len = borders.__len__()
            if borders.__len__() == 1:
                texts.append(self.drawText[borders[0]:])
            else:
                for i in range(borders.__len__()-1):
                    texts.append(self.drawText[borders[i]:borders[i+1]])
                texts.append(self.drawText[borders[-1]:])
            for txt in texts:
                srf = self.font.render(txt, True, (100,100,100))
                self.textSurfaces.append(srf)

    def arrowDown(self):
        if self.isThereAnswer:
            if self.actualAnswer < self.drawAnswers.__len__()-1:
                self.actualAnswer += 1
            else:
                self.actualAnswer = 0
        self.updateTextSurfaces()

    def arrowUp(self):
        if self.isThereAnswer:
            if self.actualAnswer > 0:
                self.actualAnswer -= 1
            else:
                self.actualAnswer = self.drawAnswers.__len__()-1
        self.updateTextSurfaces()

    # drawing is done based on the state variables
    def draw(self, screen):
        if self.drawing:
            pygame.draw.polygon(screen, (255,255,255), self.polyPoints)
            pygame.draw.polygon(screen, (100,100,100), self.polyPoints, 5)
            row = 50
            for textSurface in self.textSurfaces:
                screen.blit(textSurface, (self.drawTalkPos-280+self.offset, row))
                row += 30
        return
