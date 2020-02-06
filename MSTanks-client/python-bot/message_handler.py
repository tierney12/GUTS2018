import json
from our_tank import *



def HandleMessage(message, env, our_tank, game_state):
    if message:
        if message['MessageType'] == 'OBJECTUPDATE':

            # If the object update is our tank
            if message_relates_to_our_tank(message):
                our_tank.update(message)

            # Else add to the memory of the surrounding environment
            else:
                env.add_to_memory(message)

        elif message['MessageType'] == 'HEALTHPICKUP':
            pass

        elif message['MessageType'] == 'AMMOPICKUP':
            pass

        elif message['MessageType'] == 'SNITCHPICKUP':
            game_state.snitch_caught(message)

        elif message['MessageType'] == 'DESTROYED':
            our_tank.died()

        elif message['MessageType'] == 'ENTEREDGOAL':
            our_tank.banked_the_points()

        elif message['MessageType'] == 'KILL':
            our_tank.killed_an_enemy()

        elif message['MessageType'] == 'SNITCHCOLLECTED':
            game_state.snitch_collected()

        elif message['MessageType'] == 'SNITCHAPPEARED':
            game_state.snitch_appeared()

        elif message['MessageType'] == 'GAMETIMEUPDATE':
            pass

        elif message['MessageType'] == 'SUCCESSFULHIT':
            pass

        else:
            return



def message_relates_to_our_tank(message):
    if message['Type'] and message['Name'] and message['Type'] == 'Tank' and message['Name'] == 'ThiccThonker':
        return True
    else:
        return False
