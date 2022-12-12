#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from Guitar import Guitar

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
guitar = Guitar(ev3)
guitar.start()
print("done")
