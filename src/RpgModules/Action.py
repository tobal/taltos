
from CommonModules.Constants import Actions
from CommonModules.Constants import ActionTypes
from CommonModules.Constants import ActionData

class Action():

    def __init__(self):
        self.ACTIONS = {
                Actions.TOBALCONV : {
                        ActionData.TYPE : ActionTypes.CONVERSATION,
                        ActionData.POSITION : 0},
                Actions.GAMEINFO : {
                        ActionData.TYPE : ActionTypes.CONVERSATION,
                        ActionData.POSITION : 0},
                Actions.SHOPCONV : {
                        ActionData.TYPE : ActionTypes.CONVERSATION,
                        ActionData.POSITION : 0}
                }

    def getAction(self, action):
        if action == "karakter1action":
            return {"type" : "conversation",
                    "id"    : "karakter1conv"}
        if action == "gameinfoaction":
            return {"type" : "conversation",
                    "id"    : "game_info"}
        if action == "shopaction":
            return {"type" : "conversation",
                    "id"    : "shopconv"}
        if action == "pcaction":
            return {"type" : "gamemodechange",
                    "id"    : "cyberspace"}
