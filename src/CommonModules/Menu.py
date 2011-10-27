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
    
    def menuUp(self, langChooserAlive, chosenLanguage):
        if langChooserAlive:
            if chosenLanguage == Languages.EN:
                self.chosenLanguage = Languages.HU
            elif chosenLanguage == Languages.HU:
                self.chosenLanguage = Languages.ROV
            elif chosenLanguage == Languages.ROV:
                self.chosenLanguage = Languages.EN
    
    def menuDown(self, langChooserAlive, chosenLanguage):
        if langChooserAlive:
            if chosenLanguage == Languages.EN:
                self.chosenLanguage = Languages.ROV
            elif chosenLanguage == Languages.HU:
                self.chosenLanguage = Languages.EN
            elif chosenLanguage == Languages.ROV:
                self.chosenLanguage = Languages.HU
    
    def eventLoop(self, langChooserAlive, chosenLanguage):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:
                    self.menuUp(langChooserAlive, chosenLanguage)
                if event.key == K_s or event.key == K_DOWN:
                    self.menuDown(langChooserAlive, chosenLanguage)
                if (event.key == K_q) or (event.key == K_ESCAPE):
                    exit()
                if (event.key == K_e) or (event.key == K_RETURN):
                    if langChooserAlive:
                        self.langChooserAlive = False
                    else:
                        self.dialogAlive = False
    
    def languageChooser(self):
        self.chosenLanguage = Languages.HU
        self.langChooserAlive = True
        self.dialogAlive = True
        
        langChooserBox = Rect((150,80), (740,570))
        while self.dialogAlive:
            self.drawer.fillWithBackgroundColor(self.screen, GameModes.MENU)
            self.drawer.drawBox(langChooserBox, 3, self.screen, GameModes.MENU)
            if self.langChooserAlive:                
                languages = [Languages.HU, Languages.EN, Languages.ROV]
                textTypes = [CommonTextTypes.VAL_NYELV, CommonTextTypes.NYELV]
                languageSurfaces = []
                for language in languages:
                    oneLangSurfaces = []
                    for textType in textTypes:
                        surface = self.textDrawer.getSurfaceArrayForCommonText(textType, GameModes.MENU, language, FontSizes.BIG)
                        oneLangSurfaces.append(surface)
                    languageSurfaces.append(oneLangSurfaces)
                
                self.screen.blit(languageSurfaces[0][0][0][TextSurfaceTypes.NORMAL], (370, 150))
                self.screen.blit(languageSurfaces[1][0][0][TextSurfaceTypes.NORMAL], (330, 220))
                self.screen.blit(languageSurfaces[2][0][0][TextSurfaceTypes.NORMAL], (310, 300))
                
                surfaceTypeHu = TextSurfaceTypes.NORMAL
                surfaceTypeEn = TextSurfaceTypes.NORMAL
                surfaceTypeRov = TextSurfaceTypes.NORMAL
                
                if self.chosenLanguage == Languages.HU:
                    surfaceTypeHu = TextSurfaceTypes.INVERSE
                elif self.chosenLanguage == Languages.EN:
                    surfaceTypeEn = TextSurfaceTypes.INVERSE
                elif self.chosenLanguage == Languages.ROV:
                    surfaceTypeRov = TextSurfaceTypes.INVERSE
                    
                self.screen.blit(languageSurfaces[0][1][0][surfaceTypeHu], (460, 400))
                self.screen.blit(languageSurfaces[1][1][0][surfaceTypeEn], (460, 470))
                self.screen.blit(languageSurfaces[2][1][0][surfaceTypeRov], (460, 560))
                pygame.display.update()
            else:                
                surfaceIranyitas = self.textDrawer.getSurfaceArrayForCommonText(CommonTextTypes.IRANYITAS, GameModes.MENU, self.chosenLanguage, FontSizes.SMALL)
                
                text_pos = 100
                for surface in surfaceIranyitas:
                    self.screen.blit(surface[TextSurfaceTypes.NORMAL], (180, text_pos))
                    text_pos += 50
                pygame.display.update()
    
            self.eventLoop(self.langChooserAlive, self.chosenLanguage)
            
        return self.chosenLanguage
    
            