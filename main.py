def waterState(f):
    if f < 32:
        return "solid"
    elif f < 80:
        return "liquid"
    else:
        return "gas"
    
print(waterState(412))

def isDozen(d):
    if d % 12 == 0:
        return True
    else:
        return False

print(isDozen(60))

def toGerman(x):
    if x == "yes":
        return "ja"
    else:
        return "nein"

print(toGerman("yes"))

def stopLight(x):
    if x == "green":
        return "go"
    elif x == "yellow":
        return "slow"
    else:
        return "stop"

print(stopLight("red"))

        