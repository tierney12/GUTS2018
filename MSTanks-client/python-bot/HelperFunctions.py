from ObjectUpdateParser import *
import math
from GameServer import *

TOP_WALL = "top"
BOTTOM_WALL = "bottom"
LEFT_WALL = "left"
RIGHT_WALL = "right"

# Note: Headings are absolute
def NumTanksAimingAtUs(ourX, ourY):
    for tank in GetEnemyTanks():
        print(tank)
        enemyTurretHeading = tank['TurretHeading']
        IsTankAimingAtUs(tank, ourX, ourY)

    return 2

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
   heading = math.atan2(y2-y1,x2-x1)
   heading = rad_to_deg(heading)
   heading = (heading-360)%360
   return math.fabs(heading)


def calc_distance(ownX, ownY, otherX, otherY):
   headingX = otherX - ownX
   headingY = otherY - ownY
   return math.sqrt((headingX * headingX) + (headingY * headingY))




def RotateTurretToHeading(heading, GameServer):
    GameServer.sendMessage(ServerMessageTypes.TURNTURRETTOHEADING, {'Amount': heading})
