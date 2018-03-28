import math

def solve(equ):
    if (equ == 'sum'):
        sides = input("Please input the number of sides: ")
        d = 180 * (int(sides) - 2)
        print('The sum of the interior angles are: ' + str(d))
    elif (equ == 'each'):
        sides = input("Please input the number of sides: ")
        180 * (int(sides) - 2) / int(sides)
        print('Each interior angle measures: ' + str(d))
    elif (equ == 'ext_sum'):
        sides = input("Please input the number of sides: ")
        d = (360 * int(sides)) - (int(sides) - 2)
        print('The sum of the exterior angles are: ' + str(d))
    elif (equ == 'ext_each'):
        sides = input("Please input the number of sides: ")
        d = (360 * int(sides)) - (int(sides) - 2) / int(sides)
        print('Each exterior angle measures: ' + str(d))
