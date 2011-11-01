# The different actions are defined here

def getAction(action):
    if action == "karakter1action":
        return {"type" : "conversation",
                "id"    : "karakter1conv"}
    if action == "gameinfoaction":
        return {"type" : "conversation",
                "id"    : "game_info"}
    if action == "shopaction":
        return {"type" : "conversation",
                "id"    : "shopconv"}