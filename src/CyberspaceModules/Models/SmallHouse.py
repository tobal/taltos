
from CyberspaceModules.Geoms.Vector import Vector
from CyberspaceModules.Models.Model import Model

class SmallHouse(Model):
    def __init__(self):
        self.UVVectors = [
                Model.UV90, # front face
                Model.UV0,
                Model.UV270,
                Model.UV0,
                Model.UV90, # right face
                Model.UV0,
                Model.UV270,
                Model.UV0,
                Model.UV270, # left face
                Model.UV0,
                Model.UV90,
                Model.UV0,
                Model.UV90, # back face
                Model.UV0,
                Model.UV270,
                Model.UV0,
                Model.UV0, # front right corner
                Model.UV0,
                Model.UV0,
                Model.UV0, # front left corner
                Model.UV0,
                Model.UV0,
                Model.UV0, # back right corner
                Model.UV0,
                Model.UV0,
                Model.UV0, # back left corner
                Model.UV0,
                Model.UV0,
                Model.UV0, # top face
                Model.UV0,
                Model.UV0,
                Model.UV0,
                Model.UV0,
            ]

        self.Vectors = [
            [ # front face
                Vector(0,0,0),
                Vector(1,0,0),
                Vector(1,1,0),
                Vector(0,1,0)
            ],
            [
                Vector(1,0,0),
                Vector(2,0,0),
                Vector(2,1,0),
                Vector(1,1,0)
            ],
            [
                Vector(2,0,0),
                Vector(3,0,0),
                Vector(3,1,0),
                Vector(2,1,0)
            ],
            [
                Vector(1,1,0),
                Vector(2,1,0),
                Vector(2,2,0),
                Vector(1,2,0)
            ],
            [ # right face
                Vector(3,0,0),
                Vector(3,0,1),
                Vector(3,1,1),
                Vector(3,1,0)
            ],
            [
                Vector(3,0,1),
                Vector(3,0,2),
                Vector(3,1,2),
                Vector(3,1,1)
            ],
            [
                Vector(3,0,2),
                Vector(3,0,3),
                Vector(3,1,3),
                Vector(3,1,2)
            ],
            [
                Vector(3,1,1),
                Vector(3,1,2),
                Vector(3,2,2),
                Vector(3,2,1)
            ],
            [ # left face
                Vector(0,0,1),
                Vector(0,0,0),
                Vector(0,1,0),
                Vector(0,1,1)
            ],
            [
                Vector(0,0,2),
                Vector(0,0,1),
                Vector(0,1,1),
                Vector(0,1,2)
            ],
            [
                Vector(0,0,3),
                Vector(0,0,2),
                Vector(0,1,2),
                Vector(0,1,3)
            ],
            [
                Vector(0,1,2),
                Vector(0,1,1),
                Vector(0,2,1),
                Vector(0,2,2)
            ],
            [ # back face
                Vector(3,0,3),
                Vector(2,0,3),
                Vector(2,1,3),
                Vector(3,1,3)
            ],
            [
                Vector(2,0,3),
                Vector(1,0,3),
                Vector(1,1,3),
                Vector(2,1,3)
            ],
            [
                Vector(1,0,3),
                Vector(0,0,3),
                Vector(0,1,3),
                Vector(1,1,3)
            ],
            [
                Vector(2,1,3),
                Vector(1,1,3),
                Vector(1,2,3),
                Vector(2,2,3)
            ],
            [ # front right corner
                Vector(3,1,0),
                Vector(3,1,1),
                Vector(2,1,1),
                Vector(2,1,0)
            ],
            [
                Vector(2,1,0),
                Vector(2,1,1),
                Vector(2,3,1),
                Vector(2,2,0)
            ],
            [
                Vector(2,1,1),
                Vector(3,1,1),
                Vector(3,2,1),
                Vector(2,3,1)
            ],
            [ # front left corner
                Vector(1,1,0),
                Vector(1,1,1),
                Vector(0,1,1),
                Vector(0,1,0)
            ],
            [
                Vector(1,1,0),
                Vector(1,2,0),
                Vector(1,3,1),
                Vector(1,1,1)
            ],
            [
                Vector(0,1,1),
                Vector(1,1,1),
                Vector(1,3,1),
                Vector(0,2,1)
            ],
            [ # back right corner
                Vector(3,1,2),
                Vector(3,1,3),
                Vector(2,1,3),
                Vector(2,1,2)
            ],
            [
                Vector(3,1,2),
                Vector(2,1,2),
                Vector(2,3,2),
                Vector(3,2,2)
            ],
            [
                Vector(2,1,2),
                Vector(2,1,3),
                Vector(2,2,3),
                Vector(2,3,2)
            ],
            [ # back left corner
                Vector(1,1,2),
                Vector(1,1,3),
                Vector(0,1,3),
                Vector(0,1,2)
            ],
            [
                Vector(1,1,2),
                Vector(0,1,2),
                Vector(0,2,2),
                Vector(1,3,2)
            ],
            [
                Vector(1,1,3),
                Vector(1,1,2),
                Vector(1,3,2),
                Vector(1,2,3)
            ],
            [ # top face
                Vector(2,3,1),
                Vector(2,3,2),
                Vector(1,3,2),
                Vector(1,3,1)
            ],
            [
                Vector(1,2,0),
                Vector(2,2,0),
                Vector(2,3,1),
                Vector(1,3,1)
            ],
            [
                Vector(3,2,1),
                Vector(3,2,2),
                Vector(2,3,2),
                Vector(2,3,1)
            ],
            [
                Vector(0,2,2),
                Vector(0,2,1),
                Vector(1,3,1),
                Vector(1,3,2)
            ],
            [
                Vector(2,2,3),
                Vector(1,2,3),
                Vector(1,3,2),
                Vector(2,3,2)
            ]
        ]

        self.Lines = [
            [ # front face
                Vector(0,0,0),
                Vector(0,1,0)
            ],
            [
                Vector(0,1,0),
                Vector(1,1,0)
            ],
            [
                Vector(0,0,0),
                Vector(3,0,0)
            ],
            [
                Vector(1,1,0),
                Vector(1,2,0)
            ],
            [
                Vector(1,2,0),
                Vector(2,2,0)
            ],
            [
                Vector(2,2,0),
                Vector(2,1,0)
            ],
            [
                Vector(2,1,0),
                Vector(3,1,0)
            ],
            [ # right face
                Vector(3,0,3),
                Vector(3,0,0)
            ],
            [
                Vector(3,0,0),
                Vector(3,1,0)
            ],
            [
                Vector(3,1,0),
                Vector(3,1,1)
            ],
            [
                Vector(3,1,1),
                Vector(3,2,1)
            ],
            [
                Vector(3,2,1),
                Vector(3,2,2)
            ],
            [
                Vector(3,2,2),
                Vector(3,1,2)
            ],
            [
                Vector(3,1,2),
                Vector(3,1,3)
            ],
            [ # left face
                Vector(0,0,0),
                Vector(0,0,3)
            ],
            [
                Vector(0,0,3),
                Vector(0,1,3)
            ],
            [
                Vector(0,1,3),
                Vector(0,1,2)
            ],
            [
                Vector(0,1,2),
                Vector(0,2,2)
            ],
            [
                Vector(0,2,2),
                Vector(0,2,1)
            ],
            [
                Vector(0,2,1),
                Vector(0,1,1)
            ],
            [
                Vector(0,1,1),
                Vector(0,1,0)
            ],
            [ # back face
                Vector(0,0,3),
                Vector(3,0,3)
            ],
            [
                Vector(3,0,3),
                Vector(3,1,3)
            ],
            [
                Vector(3,1,3),
                Vector(2,1,3)
            ],
            [
                Vector(2,1,3),
                Vector(2,2,3)
            ],
            [
                Vector(2,2,3),
                Vector(1,2,3)
            ],
            [
                Vector(1,2,3),
                Vector(1,1,3)
            ],
            [
                Vector(1,1,3),
                Vector(0,1,3)
            ],
            [ # front right corner
                Vector(2,1,0),
                Vector(2,1,1)
            ],
            [
                Vector(2,1,1),
                Vector(2,3,1)
            ],
            [
                Vector(3,1,1),
                Vector(2,1,1)
            ],
            [ # front left corner
                Vector(1,1,0),
                Vector(1,1,1)
            ],
            [
                Vector(0,1,1),
                Vector(1,1,1)
            ],
            [
                Vector(1,1,1),
                Vector(1,3,1)
            ],
            [ # back right corner
                Vector(3,1,2),
                Vector(2,1,2)
            ],
            [
                Vector(2,1,3),
                Vector(2,1,2)
            ],
            [
                Vector(2,1,2),
                Vector(2,3,2)
            ],
            [ # back left corner
                Vector(0,1,2),
                Vector(1,1,2)
            ],
            [
                Vector(1,1,3),
                Vector(1,1,2)
            ],
            [
                Vector(1,1,2),
                Vector(1,3,2)
            ],
            [ # top face
                Vector(1,2,0),
                Vector(1,3,1)
            ],
            [
                Vector(2,2,0),
                Vector(2,3,1)
            ],
            [
                Vector(3,2,1),
                Vector(2,3,1)
            ],
            [
                Vector(3,2,2),
                Vector(2,3,2)
            ],
            [
                Vector(2,2,3),
                Vector(2,3,2)
            ],
            [
                Vector(1,2,3),
                Vector(1,3,2)
            ],
            [
                Vector(0,2,2),
                Vector(1,3,2)
            ],
            [
                Vector(0,2,1),
                Vector(1,3,1)
            ],
            [
                Vector(1,3,1),
                Vector(1,3,2)
            ],
            [
                Vector(1,3,2),
                Vector(2,3,2)
            ],
            [
                Vector(2,3,2),
                Vector(2,3,1)
            ],
            [
                Vector(2,3,1),
                Vector(1,3,1)
            ]
        ]

        self.Textures = [
            "../Cyber/zold_negyzet",
            "../Cyber/zold_alsoszel",
            "../Cyber/zold_2sarok_fent"
            #"../Cyber/zold_jobbszel",
            #"../Cyber/zold_balszel",
           ]

        self.TextureIndexes = [ 2,3,2,2, # front face
                2,3,2,2, # right face
                2,3,2,2, # left face
                2,3,2,2, # back face
                1,1,1, # front right corner
                1,1,1, # front left corner
                1,1,1, # back right corner
                1,1,1, # back left corner
                1,1,1,1,1 # top face
                ]

