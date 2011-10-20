# coding=utf-8

import unittest
from src.CommonModules.Texts import TextGetter
from src.CommonModules.Constants import Languages
from src.CommonModules.Constants import CommonTextTypes 

class TextGetterUnittest(unittest.TestCase):

    def setUp(self):
        self.textgetter = TextGetter.TextGetter()

    def tearDown(self):
        pass

    def test_string_reverser(self):
        baseText = "abcdefgh"
        reversedText = self.textgetter.reverseString(baseText)
        self.assertTrue(reversedText == "hgfedcba", "Text not reversed correctly")

    def test_get_hungarian_text(self):
        origText = [
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
                ]
        gotText = self.textgetter.getCommonText(CommonTextTypes.IRANYITAS, Languages.HU)
        self.assertTrue(origText == gotText, "Wrong hungarian text got")
        pass
    
    def text_get_english_text(self):
        origText = ["Choose a language"]
        gotText = self.textgetter.getCommonText(CommonTextTypes.VAL_NYELV, Languages.EN)
        self.assertTrue(origText == gotText, "Wrong english text got")
        pass
    
    def test_get_rovas_text(self):
        origText = [u"raygaM"]
        gotText = self.textgetter.getCommonText(CommonTextTypes.NYELV, Languages.ROV)
        self.assertTrue(origText == gotText, "Wrong rune text got")
        pass
