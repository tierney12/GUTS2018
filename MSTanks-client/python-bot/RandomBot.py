#!/usr/bin/python

import argparse
from env import *
from detected_object import *
from message_handler import *
from our_tank import *
from helper_functions import *
from game_state import *
from movement_helper_functions import *
from game_server import *
import time
import random

# Default values
default_name = 'ThiccThonker'
default_port = 8052
default_ip = '127.0.0.1'

# loop id's
# on each iteration of our main loop, we perform one of the three actions
MOVEMENT = 0
SHOOTING = 1

# the patrol route as a series of x y coordinate pairs
patrol_route = [
    (60, 0),
    (60, 80),
    (0, 80),
    (0, 110),
    (0, 80),
    (-60, 80),
    (-60, 0),
    (-60, -80),
    (0, -80),
    (0, -110),
    (0, -80),
    (60, -80),
]

# game state variables used to maintain the state of the game:

enemies = list([])
thonk = None
snitch = None
ammo = list([])
points_held = 0
snitch_spawned = False


print(len(patrol_route))

# Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output')
parser.add_argument('-H', '--hostname', default=default_ip, help='Hostname to connect to')
parser.add_argument('-p', '--port', default=default_port, type=int, help='Port to connect to')
parser.add_argument('-n', '--name', default=default_name, help='Name of bot')
args = parser.parse_args()

# Set up console logging
if args.debug:
    logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.DEBUG)
else:
    logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.INFO)

# Connect to game server
GameServer = ServerComms(args.hostname, args.port)

# Spawn our tank
logging.info("Creating tank with name '{}'".format(args.name))
GameServer.sendMessage(ServerMessageTypes.CREATETANK, {'Name': args.name})

# Instatiate the local environment
env = Env()
our_tank = OurTank()
game_state = GameState()

# Main loop - read game messages, ignore them and randomly perform actions
i = 0
ammoLastSeen = 60
lastTurretScan = 0
loop_action_type = MOVEMENT
current_patrol_index = 0
patrol_initialised = False

def FireWithOffset(x1, y1, x2, y2, enemy_moving_direction, GameServer):
    d = calc_distance(x1, y1, x2, y2)
    heading = get_heading(x1, y1, x2, y2)
    rotate_turret_to_heading(heading+10*math.sin(enemy_moving_direction-heading), GameServer)
    GameServer.sendMessage(ServerMessageTypes.FIRE)

def FireWithoutOffset(x1, y1, x2, y2, GameServer):
    heading = get_heading(x1, y1, x2, y2)
    rotate_turret_to_heading(heading, GameServer)
    GameServer.sendMessage(ServerMessageTypes.FIRE)

def reset_patrol(patrol_route, ourX, ourY):
    return nearest_patrol_point(patrol_route, ourX, ourY)


SNITCH_NEVER_SEEN = 0
SNITCH_CURRENTLY_SEEN = 1
SNITCH_IN_PLAY = 2

snitch_override = SNITCH_NEVER_SEEN
snitch_last_seen = 100
snitchX = 0
snitchY = 0

while True:
    # Receives the message from the server

    message = GameServer.readMessage()

    print(message)

    try:

        if message['MessageType'] and message['MessageType'] == 'SNITCHAPPEARED':
            snitch_spawned = True

        elif message['MessageType'] and message['MessageType'] == 'KILL':
            points_held = points_held + 1

        elif message['Type'] and message['Name'] and message['Type'] == 'Tank' and message['Name'] == 'ThiccThonker':
            thonk = toTank(message)

        elif message['Type'] and message['Name'] and message['Type'] == 'Tank':
            flag = False
            for i in range(len(enemies)):
                if enemies[i].name == message['Name']:
                    enemies[i] = toTank(message)
                    enemies.insert(0, enemies.pop(enemies.index(i)))
                    flag = True
                    break

            if not flag:
                enemies = [toTank(message)] + enemies

        elif message['Type'] and message['Type'] == 'AmmoPickup':
            ammo.append(toAmmo(message))


        elif message['Type'] and message['Type'] == 'Snitch':
            snitch = (message('X'), message('Y'))

        elif message['Type'] is False:
            if message == 25:
                print "don't know what this is"


    except:
        "Something went wrong!"

    print(enemies)

# If the first message has not yet been received, wait until
    if our_tank.not_received_first_update():
        continue


    if message and message['MessageType'] == 'OBJECTUPDATE' and message['Type'] == 'Snitch':
        snitch_override = SNITCH_CURRENTLY_SEEN
        snitchX = message['X']
        snitchY = message['Y']
        snitch_last_seen = 0

    ourX = our_tank.X
    ourY = our_tank.Y
    ourTurretHeading = our_tank.turret_heading
    routeX = patrol_route[current_patrol_index][0]
    routeY = patrol_route[current_patrol_index][1]

    if not patrol_initialised:
        current_patrol_index = nearest_patrol_point(patrol_route, ourX, ourY)
        patrol_initialised = True

<<<<<<< HEAD
    if loop_action_type == MOVEMENT:
        # Move out of a goal, if we're  in one
        if tank_in_goal(ourX, ourY) == "left":
            move_to_location(ourX, ourY, FRONT_OF_LEFT_GOAL[0], FRONT_OF_LEFT_GOAL[1], GameServer)
            print("moving out of left goal")
        elif tank_in_goal(ourX, ourY) == "right":
            move_to_location(ourX, ourY, FRONT_OF_RIGHT_GOAL[0], FRONT_OF_RIGHT_GOAL[1], GameServer)
            print("moving out of right goal")
        elif message and message['MessageType'] == 'OBJECTUPDATE' and message['Type'] == 'AmmoPickup':
            print("AMMO PICKUP SIGHTED")
            distance = calc_distance(ourX, ourY, message['X'], message['Y'])
            print("distance" + str(distance))
            if distance < 1000:
                print("Moving to ammo pickup-----")
                move_to_location(ourX, ourY, message['X'], message['Y'], GameServer)
                time.sleep(1)

        else:
            # Follow the default patrol route
            move_to_location(ourX, ourY, routeX, routeY, GameServer)
            print("moving along patrol route")

    if loop_action_type == SHOOTING:
        # send a shooting command
        print "shooting"
        if message and message['MessageType'] == 'OBJECTUPDATE' and message['Name'] != 'ThiccThonker' and message[
            'Type'] == 'Tank':
            # shoot him
            # FireWithOffset(ourX, ourY, message['X'], message['Y'], 0, GameServer)
            FireWithoutOffset(ourX, ourY, message['X'], message['Y'], GameServer)
            print("shooting")
        else:
            currentTurretHeading = our_tank.turret_heading
            rotate_turret_based_on_closest_wall(ourX, ourY, currentTurretHeading, GameServer)
            print("rotating turret")
=======
    if snitch_override == SNITCH_NEVER_SEEN :
        if loop_action_type == MOVEMENT:
            # Move out of a goal, if we're  in one
            if tank_in_goal(ourX, ourY) == "left":
                move_to_location(ourX, ourY, FRONT_OF_LEFT_GOAL[0], FRONT_OF_LEFT_GOAL[1], GameServer)
                print("moving out of left goal")
            elif tank_in_goal(ourX, ourY) == "right":
                move_to_location(ourX, ourY, FRONT_OF_RIGHT_GOAL[0], FRONT_OF_RIGHT_GOAL[1], GameServer)
                print("moving out of right goal")
            elif message and message['MessageType'] == 'OBJECTUPDATE' and message['Type'] == 'AmmoPickup' and snitch_override == SNITCH_NEVER_SEEN:
                 distance = calc_distance(ourX, ourY, message['X'], message['Y'])
                 print("distance" + str(distance))
                 if distance < 60:
                     print("ammo pickup available")
                     ammoLastSeen = 0
                     print("Moving to ammo pickup-----")
                     move_to_location(ourX, ourY, message['X'], message['Y'], GameServer)

            else:
                ammoLastSeen = ammoLastSeen + 1
                print("ammo last seen: " + str(ammoLastSeen))
                # Follow the default patrol route
                if ammoLastSeen > 5:
                    move_to_location(ourX, ourY, routeX, routeY, GameServer)
                    print("moving along patrol route")


        if loop_action_type == SHOOTING:
            lastTurretScan = lastTurretScan + 1
            # send a shooting command
            if message and message['MessageType'] == 'OBJECTUPDATE' and message['Name'] != 'ThiccThonker' and message['Type'] == 'Tank':
                #shoot him
                #FireWithOffset(ourX, ourY, message['X'], message['Y'], 0, GameServer)
                FireWithoutOffset(ourX, ourY, message['X'], message['Y'], GameServer)
                print("shooting")
            elif lastTurretScan >= 3:
                lastTurretScan = 0
                currentTurretHeading = our_tank.turret_heading
                rotate_turret_based_on_closest_wall(ourX, ourY, currentTurretHeading, GameServer)
                print("rotating turret")

    if snitch_override == SNITCH_CURRENTLY_SEEN:
        print("HUNTING SNITCH")
        heading_between_snitch_and_i = get_heading(ourX, ourY, snitchX, snitchY)
        # move turret to snitch
        #rotate_turret_to_heading(heading_between_snitch_and_i, GameServer)
        rotate_turret_360_degrees(ourTurretHeading, GameServer)
        # move tank to snitch
        snitchX = snitchX + (random.randint(0, 6) - 3)
        snitchY = snitchY + (random.randint(0, 6) - 3)
        move_to_location(ourX, ourY, snitchX, snitchY, GameServer)

    if snitch_override == SNITCH_IN_PLAY:
        print("sntich ** in ** play - moving to goal")
        move_to_nearest_goal(ourX, ourY, GameServer)

    snitch_last_seen = snitch_last_seen + 1
    if snitch_last_seen > 50 and snitch_override == SNITCH_CURRENTLY_SEEN:
        snitch_override = SNITCH_IN_PLAY
>>>>>>> 7fe46c0b6a9df727b11cfc59a45ee37241e417c5

    # If we're close to a point on our route, move to the next
    if is_near(ourX, ourY, routeX, routeY):
        print("---CONTINUING ALONG PATROL ROUTE")
        current_patrol_index = (current_patrol_index + 1) % len(patrol_route)

    # move to the next possible loop action type
    loop_action_type = (loop_action_type + 1) % 2
    time.sleep(0.06)
    i = i + 1
    if i > 60:
        print("patrol reset!-----------------")
        current_patrol_index = (reset_patrol(patrol_route, ourX, ourY) + 1) % len(patrol_route)
        i = 0




