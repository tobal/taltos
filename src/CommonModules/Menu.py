# coding=utf-8

import pygame
from pygame.locals import *
from src.CommonModules.Screen import ScreenDrawer
from src.CommonModules.Screen import TextDrawer
from src.CommonModules.Texts import TextGetter
from src.CommonModules.Constants import GameModes
from src.CommonModules.Constants import CommonTextTypes
from src.CommonModules.Constants import Languages

class Menu(object):
    
    def __init__(self, screen):
        self.screen = screen
        self.drawer = ScreenDrawer.ScreenDrawer()
        self.textDrawer = TextDrawer.TextDrawer()
        self.textGetter = TextGetter.TextGetter()
    
    def languageChooser(self):
        dialog = True
        hu = True
        en = False
        rov = False
        lang_choose = True
        chosenLanguage = Languages.HU
        langChooserBox = Rect((150,80), (740,570))
        while dialog:
            if lang_choose:
                self.drawer.fillWithBackgroundColor(self.screen, GameModes.MENU)
                self.drawer.drawBox(langChooserBox, 3, self.screen, GameModes.MENU)
                
                valasszEn = self.textGetter.getCommonText(CommonTextTypes.VAL_NYELV, Languages.EN)
                surfaceValasszEn = self.textDrawer.getTextArraySurfaces(valasszEn, GameModes.MENU, Languages.EN)
                valasszHu = self.textGetter.getCommonText(CommonTextTypes.VAL_NYELV, Languages.HU)
                surfaceValasszHu = self.textDrawer.getTextArraySurfaces(valasszHu, GameModes.MENU, Languages.HU)
                valasszRov = self.textGetter.getCommonText(CommonTextTypes.VAL_NYELV, Languages.ROV)
                surfaceValasszRov = self.textDrawer.getTextArraySurfaces(valasszRov, GameModes.MENU, Languages.ROV)
                
                nyelvEn = self.textGetter.getCommonText(CommonTextTypes.NYELV, Languages.EN)
                surfaceNyelvEn = self.textDrawer.getTextArraySurfaces(nyelvEn, GameModes.MENU, Languages.EN)
                nyelvHu = self.textGetter.getCommonText(CommonTextTypes.NYELV, Languages.HU)
                surfaceNyelvHu = self.textDrawer.getTextArraySurfaces(nyelvHu, GameModes.MENU, Languages.HU)
                nyelvRov = self.textGetter.getCommonText(CommonTextTypes.NYELV, Languages.ROV)
                surfaceNyelvRov = self.textDrawer.getTextArraySurfaces(nyelvRov, GameModes.MENU, Languages.ROV)
                
                font = pygame.font.Font("../resrc/fonts/gorrisans.ttf", 40)
                rovas = pygame.font.Font("../resrc/fonts/rovmajb.ttf", 70)
                self.screen.blit(surfaceValasszHu[0]['normal'], (370, 150))
                self.screen.blit(surfaceValasszEn[0]['normal'], (330, 220))
                self.screen.blit(surfaceValasszRov[0]['normal'], (310, 300))
                    
                surfaceMagyar = surfaceNyelvHu[0]['normal']
                surfaceEnglish = surfaceNyelvEn[0]['normal']
                surfaceRovas = surfaceNyelvRov[0]['normal']
                
                if chosenLanguage == Languages.HU:
                    surfaceMagyar = surfaceNyelvHu[0]['inverse']
                elif chosenLanguage == Languages.EN:
                    surfaceEnglish = surfaceNyelvEn[0]['inverse']
                elif chosenLanguage == Languages.ROV:
                    surfaceRovas = surfaceNyelvRov[0]['inverse']
                    
                self.screen.blit(surfaceMagyar, (460, 400))
                self.screen.blit(surfaceEnglish, (460, 470))
                self.screen.blit(surfaceRovas, (460, 560))
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_w or event.key == K_UP:
                            if chosenLanguage == Languages.EN:
                                chosenLanguage = Languages.HU
                            elif chosenLanguage == Languages.HU:
                                chosenLanguage = Languages.ROV
                            elif chosenLanguage == Languages.ROV:
                                chosenLanguage = Languages.EN
                        if event.key == K_s or event.key == K_DOWN:
                            if chosenLanguage == Languages.EN:
                                chosenLanguage = Languages.ROV
                            elif chosenLanguage == Languages.HU:
                                chosenLanguage = Languages.EN
                            elif chosenLanguage == Languages.ROV:
                                chosenLanguage = Languages.HU
                        if (event.key == K_q) or (event.key == K_ESCAPE):
                            exit()
                        if (event.key == K_e) or (event.key == K_RETURN):
                            if hu:
                                language = "hu"
                            elif en:
                                language = "en"
                            elif rov:
                                language = "rov"
                            lang_choose = False
            else:
                textfill = True
                text_array = []
                while textfill:
                    if language == "hu" or language == "rov":
                        text_array.append(u"     Irányítás")
                        text_array.append(u"Mozgás - Kurzornyilak, vagy WSAD")
                        text_array.append(u"Akció - Enter vagy E")
                        text_array.append(u"Kilépés - Esc vagy Q")
                        text_array.append(u" ")
                        text_array.append(u"Az akciógombbal  lehet interakcióba lépni a")
                        text_array.append(u"játéktéren lévő figurákkal, vagy tárgyakkal.")
                        text_array.append(u"A rovásírás egyelőre csak kísérleti jelleggel került")
                        text_array.append(u"a játékba.")
                        text_array.append(u" ")
                        text_array.append(u"                     <ENTER>")
                    if language == "en":
                        text_array.append(u"     Controls")
                        text_array.append(u"Movement - Cursor arrows, or WSAD")
                        text_array.append(u"Action - Enter or E")
                        text_array.append(u"Quit - Esc or Q")
                        text_array.append(u" ")
                        text_array.append(u"With the action button, you can interact with")
                        text_array.append(u"other characters or objects on the game field.")
                        text_array.append(u"The hungarian rune writing is just experimental")
                        text_array.append(u"for the time being.")
                        text_array.append(u" ")
                        text_array.append(u"                     <ENTER>")
                    textfill = False
                self.screen.fill((255,255,255))
                pygame.draw.rect(self.screen, (100,100,100), Rect((147,77), (746,576)))
                pygame.draw.rect(self.screen, (255,255,255), Rect((150,80), (740,570)))
                font = pygame.font.Font("../resrc/fonts/gorrisans.ttf", 24)
                text_pos = 100
                for text in text_array:
                    text_surface = font.render(text, True, (100,100,100))
                    self.screen.blit(text_surface, (180, text_pos))
                    text_pos += 50
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    if event.type == KEYDOWN:
                        if (event.key == K_q) or (event.key == K_ESCAPE):
                            exit()
                        if (event.key == K_e) or (event.key == K_RETURN):
                            dialog = False
                            return language
    
            