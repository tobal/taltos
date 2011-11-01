
class Conversation:

    def __init__(self):
        self.conv = []
        return

    def addText(self, id, text, whosaid, answers, end):
        # answers is a string array, whosaid and end is boolean
        # whosaid is True when the PC, False when the NPC is talking
        con = { "id" : id,
                   "text" : text,
                   "whosaid" : whosaid,
                   "answers" : answers,
                   "end" : end}
        self.conv.append(con)
        return

    def getTextsById(self, id):
        texts = []
        for i in self.conv:
            if i["id"] == str(id):
                texts.append(i)
        return texts

