import math

def solve(equ):
    for i in range(int(math.ceil(math.sqrt(equ) / 2))):
        if (i < 2):
            print (i ** i)
            if equ / (i ** i) == (equ / (i ** i)):
                print(str(int(math.sqrt(i))) + "\u221A" + str(int(equ)))
