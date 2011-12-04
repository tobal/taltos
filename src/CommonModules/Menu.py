# coding=utf-8

import pygame
from pygame.locals import *
from CommonModules.Screen import ScreenDrawer
from CommonModules.Screen import TextDrawer
from CommonModules.Texts import TextGetter
from CommonModules.Constants import GameModes
from CommonModules.Constants import CommonTextTypes
from CommonModules.Constants import Languages
from CommonModules.Constants import FontSizes
from CommonModules.Constants import TextSurfaceTypes

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
    
    def getLanguageSurfaces(self):
        languages = [Languages.HU, Languages.EN, Languages.ROV]
        textTypes = [CommonTextTypes.VAL_NYELV, CommonTextTypes.NYELV]
        languageSurfaces = []
        for language in languages:
            oneLangSurfaces = []
            for textType in textTypes:
                surface = self.textDrawer.getSurfaceArrayForCommonText(textType, GameModes.MENU, language, FontSizes.BIG)
                oneLangSurfaces.append(surface)
            languageSurfaces.append(oneLangSurfaces)
        return languageSurfaces
    
    def getSurfaceTypes(self):
        surfaceTypes = {Languages.HU : TextSurfaceTypes.NORMAL,
                        Languages.EN : TextSurfaceTypes.NORMAL,
                        Languages.ROV : TextSurfaceTypes.NORMAL}
        surfaceTypes[self.chosenLanguage] = TextSurfaceTypes.INVERSE
        return surfaceTypes
    
    def blitLangChooserText(self, languageSurfaces, surfaceTypes):
        self.screen.blit(languageSurfaces[0][0][0][TextSurfaceTypes.NORMAL], (370, 150))
        self.screen.blit(languageSurfaces[1][0][0][TextSurfaceTypes.NORMAL], (330, 220))
        self.screen.blit(languageSurfaces[2][0][0][TextSurfaceTypes.NORMAL], (310, 300))
                            
        self.screen.blit(languageSurfaces[0][1][0][surfaceTypes[Languages.HU]], (460, 400))
        self.screen.blit(languageSurfaces[1][1][0][surfaceTypes[Languages.EN]], (460, 470))
        self.screen.blit(languageSurfaces[2][1][0][surfaceTypes[Languages.ROV]], (460, 560))
    
    def languageChooser(self):
        self.chosenLanguage = Languages.HU
        self.langChooserAlive = True
        self.dialogAlive = True
        
        langChooserBox = Rect((150,80), (740,570))
        while self.dialogAlive:
            self.drawer.fillWithBackgroundColor(self.screen, GameModes.MENU)
            self.drawer.drawBox(langChooserBox, 3, self.screen, GameModes.MENU)
            if self.langChooserAlive:
                languageSurfaces = self.getLanguageSurfaces()
                surfaceTypes = self.getSurfaceTypes()
                self.blitLangChooserText(languageSurfaces, surfaceTypes)
            else:                
                surfaceIranyitas = self.textDrawer.getSurfaceArrayForCommonText(CommonTextTypes.IRANYITAS, GameModes.MENU, self.chosenLanguage, FontSizes.SMALL)
                
                text_pos = 100
                for surface in surfaceIranyitas:
                    self.screen.blit(surface[TextSurfaceTypes.NORMAL], (180, text_pos))
                    text_pos += 50
                
            pygame.display.update()
            self.eventLoop(self.langChooserAlive, self.chosenLanguage)
            
        return self.chosenLanguage
    
            
