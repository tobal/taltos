# coding=utf-8

import pygame
from pygame.locals import *
from src.CommonModules.Screen import ScreenDrawer
from src.CommonModules.Screen import TextDrawer
from src.CommonModules.Texts import TextGetter
from src.CommonModules.Constants import GameModes
from src.CommonModules.Constants import CommonTextTypes
from src.CommonModules.Constants import Languages
from src.CommonModules.Constants import FontSizes
from src.CommonModules.Constants import TextSurfaceTypes


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
                surfaceValasszEn = self.textDrawer.getTextArraySurfaces(valasszEn, GameModes.MENU, Languages.EN, FontSizes.BIG)
                valasszHu = self.textGetter.getCommonText(CommonTextTypes.VAL_NYELV, Languages.HU)
                surfaceValasszHu = self.textDrawer.getTextArraySurfaces(valasszHu, GameModes.MENU, Languages.HU, FontSizes.BIG)
                valasszRov = self.textGetter.getCommonText(CommonTextTypes.VAL_NYELV, Languages.ROV)
                surfaceValasszRov = self.textDrawer.getTextArraySurfaces(valasszRov, GameModes.MENU, Languages.ROV, FontSizes.BIG)
                
                nyelvEn = self.textGetter.getCommonText(CommonTextTypes.NYELV, Languages.EN)
                surfaceNyelvEn = self.textDrawer.getTextArraySurfaces(nyelvEn, GameModes.MENU, Languages.EN, FontSizes.BIG)
                nyelvHu = self.textGetter.getCommonText(CommonTextTypes.NYELV, Languages.HU)
                surfaceNyelvHu = self.textDrawer.getTextArraySurfaces(nyelvHu, GameModes.MENU, Languages.HU, FontSizes.BIG)
                nyelvRov = self.textGetter.getCommonText(CommonTextTypes.NYELV, Languages.ROV)
                surfaceNyelvRov = self.textDrawer.getTextArraySurfaces(nyelvRov, GameModes.MENU, Languages.ROV, FontSizes.BIG)
                
                self.screen.blit(surfaceValasszHu[0][TextSurfaceTypes.NORMAL], (370, 150))
                self.screen.blit(surfaceValasszEn[0][TextSurfaceTypes.NORMAL], (330, 220))
                self.screen.blit(surfaceValasszRov[0][TextSurfaceTypes.NORMAL], (310, 300))
                    
                surfaceMagyar = surfaceNyelvHu[0][TextSurfaceTypes.NORMAL]
                surfaceEnglish = surfaceNyelvEn[0][TextSurfaceTypes.NORMAL]
                surfaceRovas = surfaceNyelvRov[0][TextSurfaceTypes.NORMAL]
                
                if chosenLanguage == Languages.HU:
                    surfaceMagyar = surfaceNyelvHu[0][TextSurfaceTypes.INVERSE]
                elif chosenLanguage == Languages.EN:
                    surfaceEnglish = surfaceNyelvEn[0][TextSurfaceTypes.INVERSE]
                elif chosenLanguage == Languages.ROV:
                    surfaceRovas = surfaceNyelvRov[0][TextSurfaceTypes.INVERSE]
                    
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
                self.drawer.fillWithBackgroundColor(self.screen, GameModes.MENU)
                self.drawer.drawBox(langChooserBox, 3, self.screen, GameModes.MENU)
                
                iranyitasText = self.textGetter.getCommonText(CommonTextTypes.IRANYITAS, chosenLanguage)
                surfaceIranyitas = self.textDrawer.getTextArraySurfaces(iranyitasText, GameModes.MENU, chosenLanguage, FontSizes.SMALL)
                
                text_pos = 100
                for surface in surfaceIranyitas:
                    self.screen.blit(surface[TextSurfaceTypes.NORMAL], (180, text_pos))
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
    
            