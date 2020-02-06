from helper_functions import *
import time

FRONT_OF_LEFT_GOAL = (0, 80)
FRONT_OF_RIGHT_GOAL = (0, -80)

def move_to_nearest_wall(ourX, ourY, GameServer):
    nearest_wall = identify_nearest_wall(ourX, ourY)

    if nearest_wall == TOP_WALL:
        print("Closest wall is top")
        TopWallX = 65
        TopWallY = ourY
        move_to_location(ourX, ourY, TopWallX, TopWallY, GameServer)
    elif nearest_wall == BOTTOM_WALL:
        print("Closest wall is bottom")
        BottomWallX = -65
        BottomWallY = ourY
        move_to_location(ourX, ourY, BottomWallX, BottomWallY, GameServer)
    elif nearest_wall == LEFT_WALL:
        print("Closest wall is left")
        LeftWallX = ourX
        LeftWallY = 85
        move_to_location(ourX, ourY, LeftWallX, LeftWallY, GameServer)
    elif nearest_wall == RIGHT_WALL:
        print("Closest wall is right")
        RightWallX = ourX
        RightWallY = -85
        move_to_location(ourX, ourY, RightWallX, RightWallY, GameServer)


def identify_nearest_wall(ourX, ourY):
    # identify which wall is nearest, based on current coordinates
    distance_top_wall = 70 - ourX
    distance_bottom_wall = 70 + ourX
    distance_left_wall = 100 - ourY
    distance_right_wall = 100 + ourY

    minimum_distance = min(distance_top_wall, distance_bottom_wall, distance_left_wall, distance_right_wall)

    if distance_top_wall == minimum_distance:
        return "top"
    elif distance_bottom_wall == minimum_distance:
        return "bottom"
    elif distance_left_wall == minimum_distance:
        return "left"
    elif distance_right_wall == minimum_distance:
        return "right"

def rotate_turret_based_on_closest_wall(ourX, ourY, currentTurretHeading, GameServer):
    nearest_wall = identify_nearest_wall(ourX, ourY)
    if nearest_wall == TOP_WALL:
        if currentTurretHeading < 180:
            rotate_turret_to_heading(180+45, GameServer)
        else:
            rotate_turret_to_heading(180-45, GameServer)
    elif nearest_wall == BOTTOM_WALL:
        if currentTurretHeading < 360 and currentTurretHeading > 90:
            rotate_turret_to_heading(0+45, GameServer)
        else:
            rotate_turret_to_heading(360-45, GameServer)
    elif nearest_wall == LEFT_WALL:
        if currentTurretHeading < 90:
            rotate_turret_to_heading(90+45, GameServer)
        else:
            rotate_turret_to_heading(90-45, GameServer)
    elif nearest_wall == RIGHT_WALL:
        if currentTurretHeading < 270:
            rotate_turret_to_heading(270+45, GameServer)
        else:
            rotate_turret_to_heading(270-45, GameServer)

def move_to_location(ourX, ourY, locationX, locationY, GameServer):

    locationHeading = get_heading(ourX, ourY, locationX, locationY)
    GameServer.sendMessage(ServerMessageTypes.TURNTOHEADING, {'Amount': locationHeading})
    time.sleep(0.06)

    requiredDistance = calc_distance(ourX, ourY, locationX, locationY)
    GameServer.sendMessage(ServerMessageTypes.MOVEFORWARDDISTANCE, {'Amount': requiredDistance})

def move_to_nearest_goal(ourX, ourY, GameServer):
    # Move in front of the goal if our X axis value won't allow us to enter the goal
    if ourX > 10 or ourX < -10:
        if ourY > 0:
            print("moving in front of left goal")
            move_to_location(ourX, ourY, 0, 80, GameServer)
        else:
            print("moving in front of right goal")
            move_to_location(ourX, ourY, 0, -80, GameServer)
    else :
        if ourY > 0:
            # move to left goal
            print("moving into left goal")
            move_to_location(ourX, ourY, 0, 100, GameServer)
        else:
            # move to right goal
            print("moving into right goal")
            move_to_location(ourX, ourY, 0, -100, GameServer)

def move_to_centre(ourX, ourY, GameServer):
    print("moving to centre")
    print("ourX " + str(ourX) + " ourY " + str(ourY))
    move_to_location(ourX, ourY, 0.0, 0.0, GameServer)

def is_near(ourX, ourY, destinationX, destinationY):
    distance = calc_distance(ourX, ourY, destinationX, destinationY)
    return distance < 10

def nearest_patrol_point(patrol_points, ourX, ourY):
    num_points = len(patrol_points)
    closest_patrol_point_index = 0
    closest_patrol_point_distance = 200
    for i in range (0, num_points):
        pointX, pointY = patrol_points[i]
        distance = calc_distance(ourX, ourY, pointX, pointY)
        if distance < closest_patrol_point_distance:
            closest_patrol_point_index = i
            closest_patrol_point_distance = distance

    return closest_patrol_point_index

def tank_in_goal(ourX, ourY):
    if ourY > 100:
        return "left"
    if ourY < -100:
        return "right"
    else:
        return ""
