
from src.CommonModules.Constants import Directions

class RpgImages():
    TRAM = "../resrc/img/RPG/villamos.png"
    STREET_HW = "../resrc/img/RPG/hardware.png"
    STREET_INFO = "../resrc/img/RPG/utca.png"
    HARDWARE_STORE = "../resrc/img/RPG/bolt.png"
    BENCH = 4
    NOTHING = 5

class BulcsuAnimation():
    
    def __init__(self):
        self.FRAMES = {
                Directions.UP : [
                        "",
                        "",
                        ""],
                Directions.DOWN : [
                        "",
                        "",
                        "",
                        ""],
                Directions.LEFT : [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",],
                Directions.RIGHT : [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",]
        
        }
        return
    
    def getAnimationFrame(self, direction, frame):
        return self.FRAMES[direction][frame]