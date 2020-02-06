import json
from detected_object import *
from object_past import *


class Env(object):
    threshold = 1
    objects = {}

    def __init__(self, objects=None):
        if objects is None:
            objects = {}
        self.objects = objects

    def add_to_memory(self, message):
        # Convert the message into a DetectedObject
        turret_heading = message['TurretHeading']
        name = message['Name']
        heading = message['Heading']
        health = message['Health']
        type = message['Type']
        id = message['Id']
        ammo = message['Ammo']

        x = message['X']
        y = message['Y']

        # do = DetectedObject(turret_heading,
        #                name,
        #                heading,
        #                health,
        #                type,
        #                id,
        #                ammo,
        #                x,
        #                y)
        #
        # # Reserved in case Id's change
        # # for object in self.objects:
        # #     if distance_between_two_objects(do, self.objects[object]) < self.threshold:
        # #         self.objects[object].update()
        # #         return
        #
        # # If the detected object already has a past, add it to that object
        # if do.id in self.objects:
        #     self.objects[do.id].update(do)
        # else:
        #     past = ObjectPast(do)
        #     self.objects[do.id] = do

    def find_closest_enemies(self):
        pass

    def find_health_packs(self):
        pass

    def find_ammo_packs(self):
        pass