
from src.CommonModules.Constants import Languages
from src.CommonModules.Texts import CommonTexts

class TextGetter(object):

    def __init__(self):
        return

    def reverseString(self, string):
        output = string[::-1]
        return output
    
    def getCommonText(self, textType, language):
        actualLang = language
        if language == Languages.ROV:
            actualLang = Languages.HU
        actualTexts = CommonTexts.CommonTexts().TEXTS[textType][actualLang]
        output = []
        if language == Languages.ROV:
            for txt in actualTexts:
                output.append(self.reverseString(txt))
        else:
            output = actualTexts
        return output