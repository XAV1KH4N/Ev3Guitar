#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
#from Guitar import Guitar

from Neck import Neck
from Body import Body
from Guitar import Guitar, Speaker

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
guitar = Guitar(ev3)

print("done")
