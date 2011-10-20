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
        while dialog:
            if lang_choose:
                self.drawer.fillWithBackgroundColor(self.screen, GameModes.MENU)
                self.drawer.drawBox(Rect((150,80), (740,570)), 3, self.screen, GameModes.MENU)
                
                valassz_en = self.textGetter.getCommonText(CommonTextTypes.VAL_NYELV, Languages.EN)
                surface_valen = self.textDrawer.getTextArraySurfaces(valassz_en, GameModes.MENU, Languages.EN)
                valassz_hu = self.textGetter.getCommonText(CommonTextTypes.VAL_NYELV, Languages.HU)
                surface_valhu = self.textDrawer.getTextArraySurfaces(valassz_hu, GameModes.MENU, Languages.HU)
                valassz_rov = self.textGetter.getCommonText(CommonTextTypes.VAL_NYELV, Languages.ROV)
                surface_valrov = self.textDrawer.getTextArraySurfaces(valassz_rov, GameModes.MENU, Languages.ROV)
                
                nyelv_en = self.textGetter.getCommonText(CommonTextTypes.NYELV, Languages.EN)
                surface_nyen = self.textDrawer.getTextArraySurfaces(nyelv_en, GameModes.MENU, Languages.EN)
                nyelv_hu = self.textGetter.getCommonText(CommonTextTypes.NYELV, Languages.HU)
                surface_nyhu = self.textDrawer.getTextArraySurfaces(nyelv_hu, GameModes.MENU, Languages.HU)
                nyelv_rov = self.textGetter.getCommonText(CommonTextTypes.NYELV, Languages.ROV)
                surface_nyrov = self.textDrawer.getTextArraySurfaces(nyelv_rov, GameModes.MENU, Languages.ROV)
                
                font = pygame.font.Font("../resrc/fonts/gorrisans.ttf", 40)
                rovas = pygame.font.Font("../resrc/fonts/rovmajb.ttf", 70)
                self.screen.blit(surface_valhu[0]['normal'], (370, 150))
                self.screen.blit(surface_valen[0]['normal'], (330, 220))
                self.screen.blit(surface_valrov[0]['normal'], (310, 300))
    
                if hu:
                    self.screen.blit(surface_nyen[0]['inverse'], (460, 400))
                else:
                    self.screen.blit(surface_nyen[0]['normal'], (460, 400))
                if en:
                    self.screen.blit(surface_nyhu[0]['inverse'], (460, 470))
                else:
                    self.screen.blit(surface_nyhu[0]['normal'], (460, 470))
                if rov:
                    self.screen.blit(surface_nyrov[0]['inverse'], (460, 560))
                else:
                    self.screen.blit(surface_nyrov[0]['normal'], (460, 560))
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_w or event.key == K_UP:
                            if en:
                                en = False
                                hu = True
                            elif rov:
                                rov = False
                                en = True
                            elif hu:
                                hu = False
                                rov = True
                        if event.key == K_s or event.key == K_DOWN:
                            if hu:
                                hu = False
                                en = True
                            elif en:
                                en = False
                                rov = True
                            elif rov:
                                rov = False
                                hu = True
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
    
            