import datetime


class DetectedObject(object):
    # General info of object
    turret_heading = None
    name = None
    heading = None
    health = None
    type = None
    id = None
    ammo = None

    # Coordinates of object
    X = None
    Y = None
    time = None

    def __init__(self, turret_heading=None, name=None, heading=None, health=None, type=None, id=None, ammo=None, X=None,
                 Y=None):
        self.turret_heading = turret_heading
        self.name = name
        self.heading = heading
        self.health = health
        self.type = type
        self.id = id
        self.ammo = ammo

        self.X = X
        self.Y = Y
        self.time = datetime.datetime.now()

    def GetDistanceTo(self, x, y):
        # TODO: Return euclidean distance to object
        pass

    def GetHeadingTo(self, x, y):
        # TODO: Return relative heading to object
        pass

    def GetHealthOfObject(self):
        return self.health

    def GetObjectCoordinates(self):
        return self.X, self.Y

    def GetDistanceTo(self):
        # TODO: Return euclidean distance to object
        pass
