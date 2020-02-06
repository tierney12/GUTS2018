import datetime


class GameState(object):
    # General info of object
    snitch_in_play = False
    snitch_caught_by_ID = None
    game_time = None
    game_time_recorded_at = None

    def __init__(self):
        self.snitch_in_play = False
        self.game_time = 300
        self.game_time_recorded_at = datetime.datetime.now()
        self.snitch_caught_by = None

    def snitch_appeared(self):
        self.snitch_in_play = True

    def snitch_caught(self, message):
        self.snitch_in_play = False
        self.snitch_caught_by_ID = message['Id']

    def snitch_collected(self):
        self.snitch_caught_by_ID = None

    def get_game_time(self):
        return self.game_time - (datetime.datetime.now() - self.game_time_recorded_at).seconds

    def update_game_time(self, message):
        self.game_time = message['Time']
        self.game_time_recorded_at = datetime.datetime.now()
