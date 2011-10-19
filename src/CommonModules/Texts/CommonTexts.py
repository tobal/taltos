# coding=utf-8

from src.CommonModules.Constants import Languages
from src.CommonModules.Constants import CommonTextTypes

class CommonTexts():
    TEXTS = {
    CommonTextTypes.VAL_NYELV: {
                            Languages.HU:[u"Válassz nyelvet"],
                            Languages.EN:["Choose a language"]},
    CommonTextTypes.NYELV: {
                            Languages.HU:[u"Magyar"],
                            Languages.EN:["English"]},
    CommonTextTypes.IRANYITAS: {
                            Languages.HU:[
                            u"Irányítás",
                            u"Mozgás - Kurzornyilak, vagy WSAD",
                            u"Akció - Enter vagy E",
                            u"Kilépés - Esc vagy Q",
                            u" ",
                            u"Az akciógombbal  lehet interakcióba lépni a",
                            u"játéktéren lévő figurákkal, vagy tárgyakkal.",
                            u"A rovásírás egyelőre csak kísérleti jelleggel került",
                            u"a játékba.",
                            u" ",
                            u"<ENTER>"
                            ],
                            Languages.EN:[
                            u"Controls",
                            u"Movement - Cursor arrows, or WSAD",
                            u"Action - Enter or E",
                            u"Quit - Esc or Q",
                            u" ",
                            u"With the action button, you can interact with",
                            u"other characters or objects on the game field.",
                            u"The hungarian rune writing is just experimental",
                            u"for the time being.",
                            u" ",
                            u"<ENTER>"
                            ]
                }
     }
    