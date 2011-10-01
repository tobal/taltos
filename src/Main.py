# coding=utf-8

import pygame
from pygame.locals import *
from sys import exit
from pygame.time import Clock
import MainExceptions
from Rpg import RPG
from src.CommonModules import MainScreen
from src.CommonModules import MusicPlayer

def setupScreen():
    gameScreen = MainScreen.MainScreen()
    gameScreen.createScreen()
    return gameScreen

pygame.init()

MusicPlayer.MusicPlayer().playContinously()

gameScreen = setupScreen()
screen = gameScreen.getScreen()

language = "hu"
dialog = True

# game loop
while True:
    # choose language dialog
    clock = Clock()
    hu = True
    en = False
    rov = False
    lang_choose = True
    while dialog:
        if lang_choose:
            screen.fill((255,255,255))
            pygame.draw.rect(screen, (100,100,100), Rect((147,77), (746,576)))
            pygame.draw.rect(screen, (255,255,255), Rect((150,80), (740,570)))
            font = pygame.font.Font("../resrc/fonts/gorrisans.ttf", 40)
            rovas = pygame.font.Font("../resrc/fonts/rovmajb.ttf", 70)
            text_surface_hu = font.render(u"Válassz nyelvet", True, (100,100,100))
            text_surface_en = font.render("Choose a language", True, (100,100,100))
            text_surface_rov = rovas.render(u"tevleyn zssaláV", True, (100,100,100))
            text_surface_ans1 = font.render("Magyar", True, (100,100,100))
            text_surface_ans1b = font.render("Magyar", True, (255,255,255), (100,100,100))
            text_surface_ans2 = font.render("English", True, (100,100,100))
            text_surface_ans2b = font.render("English", True, (255,255,255), (100,100,100))
            text_surface_ans3 = rovas.render("raygaM", True, (100,100,100))
            text_surface_ans3b = rovas.render("raygaM", True, (255,255,255), (100,100,100))
            screen.blit(text_surface_hu, (370, 150))
            screen.blit(text_surface_en, (330, 220))
            screen.blit(text_surface_rov, (310, 300))

            if hu:
                screen.blit(text_surface_ans1b, (460, 400))
            else:
                screen.blit(text_surface_ans1, (460, 400))
            if en:
                screen.blit(text_surface_ans2b, (460, 470))
            else:
                screen.blit(text_surface_ans2, (460, 470))
            if rov:
                screen.blit(text_surface_ans3b, (460, 560))
            else:
                screen.blit(text_surface_ans3, (460, 560))
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
            screen.fill((255,255,255))
            pygame.draw.rect(screen, (100,100,100), Rect((147,77), (746,576)))
            pygame.draw.rect(screen, (255,255,255), Rect((150,80), (740,570)))
            font = pygame.font.Font("../resrc/fonts/gorrisans.ttf", 24)
            text_pos = 100
            for text in text_array:
                text_surface = font.render(text, True, (100,100,100))
                screen.blit(text_surface, (180, text_pos))
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
                        rpg = RPG.RPGModule(screen, gameScreen.getResolution(), language)

    try:
        clock.tick(30)
        rpg.game_loop()
    except MainExceptions.Exit:
        exit()

    pygame.display.update()
