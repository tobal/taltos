
from src.CommonModules.Constants import Languages
from src.CommonModules.Constants import CommonTextTypes
from src.CommonModules.Texts import CommonTexts

class TextGetter(object):

    def __init__(self):
        return

    def reverseString(self, input):
        output = input[::-1]
        return output
    
    def getCommonText(self, textType, language):
        output = []
        actualLang = language
        if language == Languages.ROV:
            actualLang = Languages.HU
        output = CommonTexts.CommonTexts().TEXTS[textType][actualLang]
        if language == Languages.ROV:
            for i in range(len(output)):
                output[i] = self.reverseString(output[i])
        return output