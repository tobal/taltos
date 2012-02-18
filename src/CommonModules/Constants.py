
class Actions():
    TOBALCONV = 0
    SHOPCONV = 1
    GAMEINFO = 2

class ActionData():
    TYPE = 0
    POSITION = 1

class ActionTypes():
    NOACTION = 0
    CONVERSATION = 1
    TRADE = 2

class Axis():
    X = 0
    Y = 1
    Z = 2

class CommonTextTypes():
    VAL_NYELV = 0
    NYELV = 1
    IRANYITAS = 2

class TextSurfaceTypes():
    NORMAL = 0
    INVERSE = 1

class RpgModes():
    WANDER = 0
    TALK = 1

class RpgScenes():
    HARDWARE = 0
    STREET = 1
    SHOP = 2

class DrawingOrder():
    FRONT = 0
    BACK = 1

class TunnelData():
    TRANSITION = 0
    SCENENAME = 1
    DROPOFF = 2
    ORIENTATION = 3

class CollisionData():
    COLLISION = 0
    POSITION = 1

class Directions():
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class GameModes():
    RPG = 0
    CYBERSPACE = 1
    WORKSHOP = 2
    HACKING = 3
    MENU = 4

class Languages():
    HU = 0
    EN = 1
    ROV = 2

class FontSizes():
    BIG = 0
    SMALL = 1

class Models():
    SMALLHOUSE = 0

class Colors():

    def __init__(self):
        return

    def getBackgroundColor(self, gameMode):
        if gameMode == GameModes.RPG:
            return (255,255,255)
        if gameMode == GameModes.MENU:
            return (255,255,255)

    def getForegroundColor(self, gameMode):
        if gameMode == GameModes.RPG:
            return (100,100,100)
        if gameMode == GameModes.MENU:
            return (100,100,100)
