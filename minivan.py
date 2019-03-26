#! usr/bin/env python3
"""
    Module 1 Task 1
    minivan.py

"""

from __future__ import print_function

def doors(carArray)
"""
   
ld => left dash
rd => right dash
cl => child lock
ml => master lock
li => left inside
lo => left outside
ri => right inside
ro => right outside
"""

    ld = int(carArray[0])
    rd = int(carArray[1])
    cl = int(carArray[2])
    ml = int(carArray[3])
    li = int(carArray[4])
    lo = int(carArray[5])
    ri = int(carArray[6])
    ro = int(carArray[7])
    gs = carArray[8]

    gear = ["P","R","N","D","1","2","3"]
    
    print("Left dashboard switch (0 or 1): {}".format(ld))
    print("Right dashboard switch (0 or 1): {}".format(rd))
    print("Child lock switch (0 or 1): {}".format(cl))
    print("Master unlock switch (0 or 1): {}".format(ml))
    print("Left inside handle (0 or 1): {}".format(li))
    print("Left outside handle (0 or 1): {}".format(lo))
    print("Right inside handle (0 or 1): {}".format(ri))
    print("Right outside handle (0 or 1): {}".format(ro))
    print("Gear shift position (P, N, D, 1, 2 ,3, or R): {}".format(gear))




def main():
    doors(1, 0, 1, 1, 0, 0, 1, 0, "P")
if __name__ == "__main__":
    main()
    exit(0)
