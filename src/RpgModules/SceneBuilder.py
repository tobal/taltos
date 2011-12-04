
from pygame import Rect
from RpgModules import Scene
from RpgModules import Objects
from RpgModules.Images.RpgImages import RpgImages
from CommonModules.Constants import RpgScenes


def buildScene(name):
    if name == RpgScenes.HARDWARE:
        bounds = Rect((5, 505), (1015, 145))
        scene = Scene.Scene(RpgImages.STREET_HW, bounds, True)
        scene.addPerson(Objects.Person(780, 360, "karakter1", 30, "karakter1action"))
        scene.addObject(Objects.ObjectSprite(100, 500, "pad1", 30))
        scene.addTunnel(Objects.TunnelObject(1010, 505, 20, 145, RpgScenes.STREET, (30,350), 0))
        scene.addTunnel(Objects.TunnelObject(590, 500, 20, 20, RpgScenes.SHOP, (550,510), 0))
    if name == RpgScenes.STREET:
        bounds = Rect(5, 505, 1015, 145)
        scene = Scene.Scene(RpgImages.STREET_INFO, bounds, True)
        scene.addTunnel(Objects.TunnelObject(0, 505, 20, 145, RpgScenes.HARDWARE, (900,350), 0))
        scene.addActionPoint(Objects.ActionMark(320, 510, 40, 40, "gameinfoaction"))
    if name == RpgScenes.SHOP:
        bounds = Rect(5, 550, 1015, 215)
        scene = Scene.Scene(RpgImages.HARDWARE_STORE, bounds, False)
        scene.addTunnel(Objects.TunnelObject(580, 750, 20, 20, RpgScenes.HARDWARE, (550,330), 0))
        scene.addActionPoint(Objects.ActionMark(255 ,540, 40, 40, "shopaction"))
        scene.addObject(Objects.ObjectSprite(-120, 530, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-123, 540, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-127, 550, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-130, 560, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-133, 570, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-137, 580, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-140, 590, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-143, 600, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-147, 610, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-150, 620, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-153, 630, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-157, 640, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-160, 650, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-163, 660, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-167, 670, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-170, 680, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-173, 690, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-177, 700, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-180, 710, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-183, 720, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-187, 730, "transp", 10))
        scene.addObject(Objects.ObjectSprite(-190, 740, "transp", 10))
    return scene
