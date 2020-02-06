from message_handler import *
import math
from game_server import *
<<<<<<< HEAD
from tank import Tank
=======
import time
>>>>>>> 7fe46c0b6a9df727b11cfc59a45ee37241e417c5

TOP_WALL = "top"
BOTTOM_WALL = "bottom"
LEFT_WALL = "left"
RIGHT_WALL = "right"

# Note: Headings are absolute
#def NumTanksAimingAtUs(ourX, ourY):
#    for tank in GetEnemyTanks():
#        print(tank)
#        enemyTurretHeading = tank['TurretHeading']
#        IsTankAimingAtUs(tank, ourX, ourY)
#
#    return 2

# Note -> this function does not currently work
def IsTankAimingAtUs(tank, ourX, ourY):
    myHeadingToEnemy = get_heading(ourX, ourY, tank['X'], tank['Y'])
    print("my heading to enemy is: ", myHeadingToEnemy)
    enemyHeadingToUs = get_heading(tank['X'], tank['Y'], ourX, ourY)
    print("enemies heading to us is: ", enemyHeadingToUs)
    print("our X " + str(ourX))
    print("our Y" + str(ourY))

def rad_to_deg(angle):
   return angle*(180.0/math.pi)

def get_heading(x1, y1, x2, y2):
   heading = math.atan2(y1-y2,x2-x1)
   heading = rad_to_deg(heading)
   heading = (heading-360)%360
   return math.fabs(heading)


def calc_distance(ownX, ownY, otherX, otherY):
   headingX = otherX - ownX
   headingY = otherY - ownY
   return math.sqrt((headingX * headingX) + (headingY * headingY))

def rotate_turret_to_heading(heading, GameServer):
    GameServer.sendMessage(ServerMessageTypes.TURNTURRETTOHEADING, {'Amount': heading})
<<<<<<< HEAD

def toTank(message):
    return Tank(message['TurretHeading'], message['Name'], message['Heading'], message['Health'], message['Type'],
                message['Id'], message['Ammo'], message['X'], message['Y'])

def toAmmo(message):
    return (message['X'], message['Y'])
=======
    time.sleep(0.06)

def rotate_turret_360_degrees(currentHeading, GameServer):
    if currentHeading < 180:
        rotate_turret_to_heading(359, GameServer)
    else:
        rotate_turret_to_heading(179, GameServer)
>>>>>>> 7fe46c0b6a9df727b11cfc59a45ee37241e417c5
