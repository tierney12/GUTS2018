class Ammo(object):
    # General info of object

    # Coordinates of object
    X = None
    Y = None

    def __init__(self, turret_heading=None, name=None, heading=None, health=None, type=None, id=None, ammo=None, X=None,
                 Y=None):
        self.turret_heading = turret_heading
        self.name = name
        self.heading = heading
        self.health = health
        self.type = type
        self.id = id
        self.ammo = ammo
        self.points_held = 0
        self.points_banked = 0
        self.points_to_collect = False

        self.X = X
        self.Y = Y