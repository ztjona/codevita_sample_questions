# -*- coding: utf-8 -*-
'''
Python 3.8.6
[MSC v.1916 64 bit (AMD64)]
08 / 12 / 2020
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from math import pi, sqrt
''' 

################################################### '''


def calculateArc(x0, y0, z0, x1, y1, z1):
    ''' An arc that has an angle of 60º at the center.
    Hence the radious is the same as the arc distance
    ############################################### '''
    r = sqrt((x1-x0)**2 + (y1-y0)**2+ (z1-z0)**2)

    return pi/3*r


def findFace(x, y, z):
    ''' returns a code of the face
    "x0"
    "x10", "y0",...
    ############################################### '''
    if x == 0:
        return 'x0'
    elif x == 10:
        return 'x10'
    elif y == 0:
        return 'y0'
    elif y == 10:
        return 'y10'
    elif z == 0:
        return 'z0'
    elif z == 10:
        return 'z10'


def calculateDistance(x0, y0, z0, x1, y1, z1):
    ''' When the bug needs to move in the same face it does an arc.
    When it needs to go to a different face, it goes the shortest path.
    
    ############################################### '''
    face0 = findFace(x0, y0, z0)
    face1 = findFace(x1, y1, z1)
    
    if face0 == face1:
        # in the same face!
        return calculateArc(x0, y0, z0, x1, y1, z1)

    # else: points are in different faces!

    # are in opposite faces???
    if (face0 == 'x0' and face1=='x10') or (face0 == 'x10' and face1=='x0'):
        # in opposite faces of the x plane, goes trhoguh the z up plane
        return sqrt((y1-y0)**2 + (10 - z1 + 10 - z0 + 10)**2)

    if (face0 == 'y0' and face1=='y10') or (face0 == 'y10' and face1=='y0'):
        # in opposite faces of the y plane, goes trhoguh the z up plane
        return sqrt((x1-x0)**2 + (10 - z1 + 10 - z0 + 10)**2)

    # else: points are in adjacent faces!
    if (face0 == 'x0' and face1=='y0') or (face1 == 'x0' and face0=='y0'):
        # ya q un x y un y son cero tncs si vale
        return sqrt((x1 + x0 + y1 + y0)**2 + (z1 - z0)**2)

    if (face0 == 'x0' and face1=='y10') or (face1 == 'x0' and face0=='y10'):
        # ya q 1 y is 10 and 1 x is cero
        return sqrt((x1 + x0 + abs(y1 - y0))**2 + (z1 - z0)**2)

    if (face0 == 'x0' and face1=='z10') or (face1 == 'x0' and face0=='z10'):
        return sqrt((x1 + x0 + abs(z1 - z0))**2 + (y1 - y0)**2)

    if (face0 == 'x10' and face1=='y0') or (face1 == 'x10' and face0=='y0'):
        return sqrt((y1 + y0 + abs(x1 - x0))**2 + (z1 - z0)**2)
        
    if (face0 == 'x10' and face1=='y10') or (face1 == 'x10' and face0=='y10'):
        return sqrt((abs(y1 - y0) + abs(x1 - x0))**2 + (z1 - z0)**2)
        
    if (face0 == 'x10' and face1=='z10') or (face1 == 'x10' and face0=='z10'):
        return sqrt((abs(x1 - x0) + abs(z1 - z0))**2 + (y1 - y0)**2)


def main():
    ''' 
    
    ############################################### '''
    N = int(input())
    vals = list(map(float, input().split(",")))

    x0, y0, z0 = vals[0:3]
    dist = 0
    for i in range(1, N):
        x, y, z = vals[i*3:(i + 1)*3]

        dist += round(calculateDistance(x0, y0, z0, x, y, z), 2)
        x0, y0, z0 = x, y, z
    
    print(dist)
    return


if __name__ == "__main__":
    main()
