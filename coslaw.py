# This code is 🔥

import math
import webbrowser
from sympy import preview

def solve(equ):
    if (equ == 'cos'):
        c = float(input("Please input the angle: "))
        a = float(input("Please input Side 1: "))
        b = float(input("Please input Side 2: "))
        # Law of cosines
        d = math.sqrt(((a ** 2) + (b ** 2)) - (2 * (a * b) * math.cos(math.radians(c))))
        # step1 = sqrt(a ** 2 + b ** 2 - 2 * (a) * (b) * cos(c))
        # step2 = sqrt((a ** 2) + (b ** 2) + -(2))
        print("The opposite side is: " + str(d))
        print('Step by step instructions are opening in your browser.')
    elif (equ == 'sin'):
        a = float(input("Please input opposite angle: "))
        b = float(input("Please input other opposite angle: "))
        c = float(input("Please input the side: "))
        # law of sins
        d = c * math.sin(math.radians(b)) / math.sin(math.radians(a))
        print("The opposite side is: " + str(d))
    elif (equ == 'rsin'):
        a = float(input("Please input the angle: "))
        b = float(input("Please input opposite side: "))
        c = float(input("Please input side 2: "))
        # law of rsins
        d = math.asin((c * math.sin(math.radians(a)) / b))
        print("The angle is: " + str(math.degrees(d)))
    elif (equ == 'rcos'):
        a = float(input("Please input side 1: "))
        b = float(input("Please input side 2: "))
        c = float(input("Please input opposite side: "))
        # law of rcos
        d = math.acos(((a * a) + (b * b) - (c * c)) / (2 * (a * b)))

    elif (equ == 'dis'):
        # Get X1 and Y1
        x1 = float(input("Please input X1: "))
        y1 = float(input("Please input Y1: "))
        x2 = float(input("Please input X2: "))
        y2 = float(input("Please input Y2: "))
        # Solve using distance forumula
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print("The distance is: " + str(d))
        if y2 - y1 != 0:
            print("The slope is: " + str((x2 - x1)/(y2 - y1)))
        else:
            print("The slope is: " + str(x2 - x1))

    elif (equ == 'cancel'):
        print('Canceling')
