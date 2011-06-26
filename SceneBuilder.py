import Scene
import Objects

def build_scene(name):
    if name == "hardware":
        scene = Scene.Scene("hardware", "img/hardware.png", [505, 650, 5, 1020], True)
        scene.add_person(Objects.Person(780, 360, "karakter1", 30, "karakter1action"))
        scene.add_object(Objects.ObjectSprite(100, 500, "pad1", 30))
        scene.add_tunnel(Objects.TunnelObject(1010, 505, 20, 145, "street", (30,350), 0))
        scene.add_tunnel(Objects.TunnelObject(590, 500, 20, 20, "shop", (550,510), 0))
    if name == "street":
        scene = Scene.Scene("street", "img/utca.png", [505, 650, 5, 1020], True)
        scene.add_tunnel(Objects.TunnelObject(0, 505, 20, 145, "hardware", (900,350), 0))
        scene.add_actionpoint(Objects.ActionMark(320, 510, 40, 40, "gameinfoaction"))
    if name == "shop":
        scene = Scene.Scene("shop", "img/bolt.png", [550, 765, 5, 1020], False)
        scene.add_tunnel(Objects.TunnelObject(580, 750, 20, 20, "hardware", (550,330), 0))
        scene.add_actionpoint(Objects.ActionMark(255 ,540, 40, 40, "shopaction"))
        scene.add_object(Objects.ObjectSprite(-120, 530, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-123, 540, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-127, 550, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-130, 560, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-133, 570, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-137, 580, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-140, 590, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-143, 600, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-147, 610, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-150, 620, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-153, 630, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-157, 640, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-160, 650, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-163, 660, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-167, 670, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-170, 680, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-173, 690, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-177, 700, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-180, 710, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-183, 720, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-187, 730, "transp", 10))
        scene.add_object(Objects.ObjectSprite(-190, 740, "transp", 10))
    return scene
