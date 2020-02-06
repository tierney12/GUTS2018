import datetime
from collections import deque


class ObjectPast(object):
    # General info of object
    id = 0
    max = 20
    detected_objects = deque()
    last_updated = None

    def __init__(self, detected_object):
        self.detected_objects.append(detected_object)
        self.last_updated = datetime.datetime.now()
        self.id = detected_object['Id']

    def update(self, detected_object):
        # To avoid taking too much memory, keep the queue at a max of 20 past states
        if len(self.detected_objects) >= self.max:
            self.detected_objects.pop()
        self.detected_objects.append(detected_object)
        self.last_updated = datetime.datetime.now()

    def get_first_object(self):
        if self.detected_objects and self.detected_objects[0]:
            return self.detected_objects[0]

    def get_second_object(self):
        if self.detected_objects and self.detected_objects[1]:
            return self.detected_objects[1]

    def get_third_object(self):
        if self.detected_objects and self.detected_objects[2]:
            return self.detected_objects[2]

    def get_nth_object(self, n):
        if self.detected_objects and self.detected_objects[n]:
            return self.detected_objects[n]
