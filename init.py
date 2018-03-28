COSLAW = __import__('coslaw')
BRAD = __import__('brad')
GEO = __import__('geo')
# psqr    = __import__('psqr')

print("Welcome to the Geometry Toolkit\n==============================\nCreated by: Avery Wagar & Erik Anderson")

DONE = False
while not DONE:
    choice = input("What tool would you like to use? (radical, trig, geo) or type quit to exit > ")

    if choice == "trig":
        COSLAW.solve(input("What equation would you like to solve? (sin, cos, rsin, rcos, dis) or type cancel to cancel > "))
    elif choice == "radical":
        BRAD.solve(float(input("Please enter your number: ")))
    elif choice == "geo":
        GEO.solve(input("Which equation would you like to solve? (sum, each, ext_sum,
                        ext_each) > "))
    elif choice == "clear":
        import os
        clear = lambda: os.system('clear')
        clear()
        print("Welcome to the Geometry Toolkit\n==============================\nCreated by: Avery Wagar & Erik Anderson")
    elif choice == 'quit':
        DONE = True
        print('Goodbye!')
