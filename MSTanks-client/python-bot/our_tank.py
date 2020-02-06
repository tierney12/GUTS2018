class OurTank(object):
    # General info of object
    turret_heading = None
    name = None
    heading = None
    health = None
    type = None
    id = None
    ammo = None
    points_held = 0
    points_banked = 0
    points_to_collect = False

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

    def update(self, message):
        if message and message['X']:
            self.X = message['X']
        if message and message['Y']:
            self.Y = message['Y']
        if message and message['TurretHeading']:
            self.turret_heading = message['TurretHeading']

    def holding_points(self):
        return self.points_to_collect

    def killed_an_enemy(self):
        self.points_held += 1
        self.points_to_collect = True

    def died(self):
        self.points_held = 0
        self.points_to_collect = False

    def banked_the_points(self):
        self.points_banked += self.points_held
        self.points_to_collect = False

    def get_number_of_points_held(self):
        return self.points_held

    def get_number_of_points_banked(self):
        return self.points_banked

    def not_received_first_update(self):
        if not self.X and not self.Y:
            return True
        else:
            return False