# coding=utf-8

from RpgModules import Conversation
from CommonModules.Constants import Languages

class Conversations:

    def __init__(self, conv, lang):
        self.conversation = self.generateConversation(conv, lang)
        self.strCounter = 0
        self.strList = []
        return

    def generateConversation(self, conversation, language):
        conv = Conversation.Conversation()
        if language == Languages.EN:
            if conversation == "shopconv":
                conv.addText("1",
                              u"Hi, I'm the hardware dealer. In the game you can buy everything you need for your computer from me.",
                              False, [], False)
                conv.addText("1",
                              u"But for now, all you can do is read this crap over and over again, cuz Tobal was too lazy to implement shopping.",
                              False, [], True)
                return conv
            if conversation == "game_info":
                conv.addText("1",
                              u"Programming, graphics, design: Tobal",
                              True, [], False)
                conv.addText("1",
                              u"Music is made by Akpoh",
                              True, [], False)
                conv.addText("1",
                              u"Akpoh is a goa musician, and the intellectual founder of the Love Peace Freedom goa movement. The music is released under Creative Commons 2.5 licence.",
                              True, [], False)
                conv.addText("1",
                              u"You can find Akpoh's webpage here: http://lovepeacefreedom. lapunk.hu/",
                              True, [], False)
                conv.addText("1",
                              u"The game is developed in python, with pyGame and pyOpenGL. The main graphics is drawn with hand, then scanned and edited using Gimp.",
                              True, [], False)
                conv.addText("1",
                              u"Táltos is an open source project, so you can contribute to it in any way you want. You can see the project page on launchpad: https:// launchpad.net/taltos. The code is released under GPL v3 licence.",
                              True, [], False)
                conv.addText("1",
                              u"You can e-mail the developer using this address: <tobal17 @gmail.com>, and you can follow him on identi.ca (accname is tobal) too.",
                              True, [], True)
                return conv
            if conversation == "karakter1conv":
                conv.addText("1",
                              "Hi. Who are you?",
                              True, [], False)
                conv.addText("1",
                              "I'm Tobal, I made this game.",
                              False, [], False)
                conv.addText("1",
                              "",
                              True, [["I have some questions","2"]], False)
                answ = [
                        ["Do you look like this in real?", "21"],
                        ["Did you make the whole game?","22"],
                        ["Why can't I do more things?","23"],
                        ["What can I expect from the complete game?","24"],
                        ["Bye","25"]
                        ]
                conv.addText("2",
                              "",
                              True, answ, False)
                conv.addText("21",
                              "No, in the real world I have bigger belly and my hair is much less cool.",
                              False, [], False)
                conv.addText("21",
                              "",
                              True, [["I see","2"]], False)
                conv.addText("22",
                              u"No, the music you hear is made by Akpoh (Krisztián Holpert), who is a goa musican, and he gave this music for free to the game.",
                              False, [], False)
                conv.addText("22",
                              "",
                              True, [["I see","2"]], False)
                conv.addText("23",
                              "Because this is just a tech demo, with which I want to demonstrate the 'wandering' part of the game.",
                              False, [], False)
                conv.addText("23",
                              "",
                              True, [["I see","2"]], False)
                conv.addText("24",
                              "This tech demo only shows one module of the whole game. The title of the game will be Taltos.",
                              False, [], False)
                conv.addText("24",
                              "",
                              True, [["Tell me about it","30"]], False)
                answ = [
                        ["What is the game's setting?", "261"],
                        ["What other modules will be in the game?","262"],
                        ["What will be the game's plot about?","263"],
                        ["What does the game's title means?","264"],
                        ["Bye","25"]
                        ]
                conv.addText("30",
                              "",
                              True, answ, False)
                conv.addText("261",
                              "The game is a cyberpunk hacker/RPG game, and it takes place in Miskolc, present time.",
                              False, [], False)
                conv.addText("261",
                              "",
                              True, [["I see","30"]], False)
                conv.addText("262",
                              "This part of the game realizes the 'wandering' part of the game. Here the player can wander in the city, talk with other people, and buy hardware.",
                              False, [], False)
                conv.addText("262",
                              "In an other part the player can assemble his own computer, from parts, and can solder his own adapter cards.",
                              False, [], False)
                conv.addText("262",
                              "There will be a hacking module, which is the main part of the game. Here the player will have to break into systems and get information.",
                              False, [], False)
                conv.addText("262",
                              "And lastly, in the cyberspace part, the player can travel in the 3D world of cyberspace, can break into systems (Neuromancer style), and get information.",
                              False, [], False)
                conv.addText("262",
                              "",
                              True, [["I see","30"]], False)
                conv.addText("263",
                              "The player takes the role of a hacker, who is fighting against the moneyed oligarchies, but supernatural forces also help him.",
                              False, [], False)
                conv.addText("263",
                              "The fantasy aspect of the game is based on the ancient hungarian mithology.",
                              False, [], False)
                conv.addText("263",
                              "",
                              True, [["I see","30"]], False)
                conv.addText("264",
                              u"The táltos is the shaman, or mage in ancient hungarian society.",
                              False, [], False)
                conv.addText("264",
                              "",
                              True, [["I see","30"]], False)
                conv.addText("25",
                              "Bye",
                              False, [], True)
                return conv
        if language == Languages.HU:
            if conversation == "shopconv":
                conv.addText("1",
                              u"Szia, én vagyok a hardver kereskedő. A játékban majd tőlem vehetsz meg minden cuccot, ami a gépedbe kell majd.",
                              False, [], False)
                conv.addText("1",
                              u"Most viszont csak ezt a szöveget olvashatod újra és újra, mert Tobal lusta volt ahhoz, hogy a vásárlást lefejlessze.",
                              False, [], True)
                return conv
            if conversation == "game_info":
                conv.addText("1",
                              u"Programozás, grafika, tervezés: Tobal",
                              True, [], False)
                conv.addText("1",
                              u"A játék zenéjét Akpoh készítette.",
                              True, [], False)
                conv.addText("1",
                              u"Akpoh egy goa zenész, ezen kívül a szellemi alapítója a Love Peace Freedom goa mozgalomnak. A zenére a Creative Commons 2.5 licensz érvényes.",
                              True, [], False)
                conv.addText("1",
                              u"Akpoh weboldalát megtalálod itt: http://lovepeacefreedom. lapunk.hu/",
                              True, [], False)
                conv.addText("1",
                              u"A játék python nyelven íródott, pyGame és pyOpenGL API-val. A legtöbb grafika kézzel festett, és Gimp-el szerkesztett.",
                              True, [], False)
                conv.addText("1",
                              u"A Táltos egy nyílt forráskódú projekt, így bárki bárhogy részt vehet benne. A projekt weboldalát megtalálod launchpad-en: https:// launchpad.net/taltos. A forráskód a GPL v3 hatálya alá tartozik.",
                              True, [], False)
                conv.addText("1",
                              u"Írhatsz e-mailt a fejlesztőnek erre a címre: <tobal17 @gmail.com>, vagy követheted identi.ca-n (tobal néven)",
                              True, [], True)
                return conv
            if conversation == "karakter1conv":
                conv.addText("1",
                              u"Szeva, te ki vagy?",
                              True, [], False)
                conv.addText("1",
                              u"Tobal vagyok, én készítettem ezt a játékot",
                              False, [], False)
                conv.addText("1",
                              "",
                              True, [[u"Lenne pár kérdésem","2"]], False)
                answ = [
                        [u"Te a való életben is így nézel ki?", "21"],
                        [u"Az egész játékot te csináltad?","22"],
                        [u"Miért csak ilyen kevés dolgot tudok csinálni?","23"],
                        [u"Mit várhatok majd a teljes játéktól?","24"],
                        [u"Viszlát","25"]
                        ]
                conv.addText("2",
                              "",
                              True, answ, False)
                conv.addText("21",
                              u"Nem, a valóságban nagyobb a pocakom, és a hajam se ilyen menő",
                              False, [], False)
                conv.addText("21",
                              "",
                              True, [[u"Értem","2"]], False)
                conv.addText("22",
                              u"Nem, a zenét, amit hallassz, Akpoh, vagyis Holpert Krisztián készítette, aki egy lelkes goa zenész, és ingyen felajánlotta a zenéit a játékhoz",
                              False, [], False)
                conv.addText("22",
                              "",
                              True, [[u"Értem","2"]], False)
                conv.addText("23",
                              u"Mert ez csak egy tech demó, amivel demonstrálom, hogy hogyan fog kinézni a játék mászkálós része",
                              False, [], False)
                conv.addText("23",
                              "",
                              True, [[u"Értem","2"]], False)
                conv.addText("24",
                              u"A teljes játéknak ez a tech demó csak egy részét, egy modulját mutatja be. A játék címe Táltos lesz.",
                              False, [], False)
                conv.addText("24",
                              "",
                              True, [[u"Mesélj még erről.","30"]], False)
                answ = [
                        [u"Milyen környezetben játszódik majd a játék?", "261"],
                        [u"Milyen más modulok lesznek még a játékban?","262"],
                        [u"Mi lesz a játék sztorija?","263"],
                        [u"Mit jelent a játék címe?","264"],
                        [u"Viszlát","25"]
                        ]
                conv.addText("30",
                              "",
                              True, answ, False)
                conv.addText("261",
                              u"A játék egy cyberpunk hacker/szerepjáték lesz, és napjainkban játszódik Miskolcon.",
                              False, [], False)
                conv.addText("261",
                              "",
                              True, [[u"Értem","30"]], False)
                conv.addText("262",
                              u"Ez a része a játéknak a városban való mászkálást valósítja meg. Itt lehet a városban mozogni, beszélgetni az emberekkel és különböző cuccokat vásárolni.",
                              False, [], False)
                conv.addText("262",
                              u"A játék egy másik részében a játékos részegységenként összeállíthatja saját számítógépét, és saját adapter kártyákat forraszthat össze.",
                              False, [], False)
                conv.addText("262",
                              u"Lesz egy hacking modul, ami a játék gerincét adja, itt a játékosnak a számítógépével rendszereket kell feltörnie és információkat szerezhet.",
                              False, [], False)
                conv.addText("262",
                              u"Végül a cyberspace részben a játékos a 3D-s kiberteret járhatja be. Ott is rendszereket törhet fel (Neurománc stílusban), és infókat szerezhet.",
                              False, [], False)
                conv.addText("262",
                              "",
                              True, [[u"Értem","30"]], False)
                conv.addText("263",
                              u"A játékos egy hacker bőrébe bújik, aki összetűzésbe kerül a nagypénzes oligarchiával, de természetfeletti erők is a segítségére sietnek.",
                              False, [], False)
                conv.addText("263",
                              u"A játék fantasy elemei az ősmagyar mitológiát veszik alapul.",
                              False, [], False)
                conv.addText("263",
                              "",
                              True, [[u"Értem","30"]], False)
                conv.addText("264",
                              u"A táltos az ősmagyarok sámánja, vagyis pontosabban mágusa volt.",
                              False, [], False)
                conv.addText("264",
                              "",
                              True, [[u"Értem","30"]], False)
                conv.addText("25",
                              u"Szeva",
                              False, [], True)
                return conv
        if language == Languages.ROV:
            if conversation == "shopconv":
                conv.addText("1",
                              u"Szia, én vagyok a hardver kereskedő. A játékban majd tőlem vehetsz meg minden cuccot, ami a gépedbe kell majd.",
                              False, [], False)
                conv.addText("1",
                              u"Most viszont csak ezt a szöveget olvashatod újra és újra, mert Tobal lusta volt ahhoz, hogy a vásárlást lefejlessze.",
                              False, [], True)
                return conv
            if conversation == "game_info":
                conv.addText("1",
                              u"Programozás, grafika, tervezés: Tobal",
                              True, [], False)
                conv.addText("1",
                              u"A játék zenéjét Akpoh készítette.",
                              True, [], False)
                conv.addText("1",
                              u"Akpoh egy goa zenész, ezen kívül a szellemi alapítója a Love Peace Freedom goa mozgalomnak.",
                              True, [], False)
                conv.addText("1",
                              u"Akpoh weboldalát megtalálod itt: http://lovepeacefreedom. lapunk.hu/",
                              True, [], False)
                conv.addText("1",
                              u"A játék python nyelven íródott, pyGame és pyOpenGL API-val. A legtöbb grafika kézzel festett, és Gimp-el szerkesztett.",
                              True, [], False)
                conv.addText("1",
                              u"A Táltos egy nyílt forráskódú projekt, így bárki bárhogy részt vehet benne. A projekt weboldalát megtalálod launchpad-en: https:// launchpad.net/taltos",
                              True, [], False)
                conv.addText("1",
                              u"Írhatsz e-mailt a fejlesztőnek erre a címre: <tobal17 @gmail.com>, vagy követheted identi.ca-n (tobal néven)",
                              True, [], True)
                return conv
            if conversation == "karakter1conv":
                conv.addText("1",
                              u"?ygav ik et ,avezS",
                              True, [], False)
                conv.addText("1",
                              u"tokétáj a tze mettetízsék né ,koygav laboT",
                              False, [], False)
                conv.addText("1",
                              "",
                              True, [[u"mesédrék ráp enneL","2"]], False)
                answ = [
                        [u"?ik lezén ygí si nebtelé ólav a eT", "21"],
                        [u"?datlánisc et tokétáj zsége zA","22"],
                        [u"?inlánisc kodut toglod sévek neyli kasc tréiM","23"],
                        [u"?lótkétáj sejlet a djam kotahráv tiM","24"],
                        [u"tálzsiV","25"]
                        ]
                conv.addText("2",
                              "",
                              True, answ, False)
                conv.addText("21",
                              u"őnem neyli es majah a sé ,mokacop a bboygan nabgásólav a ,meN",
                              False, [], False)
                conv.addText("21",
                              "",
                              True, [[u"metrÉ","2"]], False)
                conv.addText("22",
                              u"zohkétáj a tiénez a attolnájalef neygni sé ,zsénez aog seklel yge ika ,ettetízsék náitzsirK treploH siygav ,hopkA ,zssallah tima ,ténez a ,meN",
                              False, [], False)
                conv.addText("22",
                              "",
                              True, [[u"metrÉ","2"]], False)
                conv.addText("23",
                              u"ezsér sólákzsám kétáj a inzénik gof naygoh ygoh ,molártsnomed levima ,ómed hcet yge kasc ze treM",
                              False, [], False)
                conv.addText("23",
                              "",
                              True, [[u"metrÉ","2"]], False)
                conv.addText("24",
                              u".zsel sotláT emíc kétáj A .eb ajtatum tájludom yge ,tézsér yge kasc ómed hcet a ze kankétáj sejlet A",
                              False, [], False)
                conv.addText("24",
                              "",
                              True, [[u"lőrre gém jléseM","30"]], False)
                answ = [
                        [u"?kétáj a djam kidózstáj nebtezeynrök neyliM", "261"],
                        [u"?nabkétáj a gém kenzsel koludom sám neyliM","262"],
                        [u"?ajirotzs kétáj a zsel iM","263"],
                        [u"?emíc kétáj a tnelej tiM","264"],
                        [u"tálzsiV","25"]
                        ]
                conv.addText("30",
                              "",
                              True, answ, False)
                conv.addText("261",
                              u".nocloksiM kidózstáj nabkniajpan sé ,zsel kétájperezs/rekcah knuprebyc yge kétáj A",
                              False, [], False)
                conv.addText("261",
                              "",
                              True, [[u"metrÉ","30"]], False)
                conv.addText("262",
                              u".inlorásáv takoccuc őzöbnölük sé lekkerebme za integlézseb ,ingozom nabsoráv a tehel ttI .gem ajtísólav tsálákzsám ólav nabsoráv a kankétáj a ezsér a zE",
                              False, [], False)
                conv.addText("262",
                              u".ezssö tahtzsarrof takáytrák retpada tájas sé ,tépégótímázs tájas ajtahtílláezssö tnéknegésygezsér sokétáj a nebézsér kisám yge kétáj A",
                              False, [], False)
                conv.addText("262",
                              u".tehzerezs takóicámrofni sé einrötlef llek tekerezsdner levépégótímázs a kansokétáj a tti ,ajda técnireg kétáj a ima ,ludom gnikcah yge zseL",
                              False, [], False)
                conv.addText("262",
                              u".tehzerezs takófni sé ,)nabsulíts cnámorueN( lef tehröt tekerezsdner si ttO .eb ajtahráj teretrebik s-D3 a sokétáj a nebzsér ecapsrebyc a lügéV",
                              False, [], False)
                conv.addText("262",
                              "",
                              True, [[u"metrÉ","30"]], False)
                conv.addText("263",
                              u".kenteis erégéstíges a si kőre itteleftezsémret ed ,laváihcragilo seznépygan a lürek ebsézűtezssö ika ,kijúb ebérőb rekcah yge sokétáj A",
                              False, [], False)
                conv.addText("263",
                              u".lupala kizsev táigólotim raygamső za iemele ysatnaf kétáj A",
                              False, [], False)
                conv.addText("263",
                              "",
                              True, [[u"metrÉ","30"]], False)
                conv.addText("264",
                              u".tlov asugám nabbasotnop siygav ,ajnámás koraygamső za sotlát A",
                              False, [], False)
                conv.addText("264",
                              "",
                              True, [[u"metrÉ","30"]], False)
                conv.addText("25",
                              u"avezS",
                              False, [], True)
                return conv
        return

    def getNextString(self, id):
        if self.strCounter == 0:
            self.strList = self.conversation.getTextsById(id)
        str = self.strList[self.strCounter]
        if self.strCounter + 1 >= len(self.strList):
            self.strCounter = 0
            self.strList = []
        else:
            self.strCounter += 1
        return str
