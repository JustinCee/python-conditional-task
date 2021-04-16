speed = float(input("What was your speed in km/h?:"))
allowed = float(input("What was the allowed speed on the road?:"))

points = (speed - allowed)/5

if speed <=60:
    print("OK")

if points < 12:
    print("demerit: " + str(points))

else:
    print("time to go to jail")

