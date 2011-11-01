
from src.CommonModules.Constants import Directions

class RpgImages(object):
    TRAM = "../resrc/img/RPG/villamos.png"
    STREET_HW = 1
    STREET_INFO = 2
    HARDWARE_STORE = 3
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