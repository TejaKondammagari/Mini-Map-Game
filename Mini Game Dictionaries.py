# This is a mini game based on a map in section 9, video 57.

locations={ 0: "You are sitting in front of a computer learning python",
            1: "You are standing at the end of a roof before a small brick building",
            2: "You are at the top of the hill",
            3: "You are inside a building, a well house for a small stream",
            4: "You are in a valley beside a stream",
            5: "You are in the forest"}

exits= [{"Q":0},
        {"W":2, "E":3, "N":5, "S":4, "Q":0},
        {"N":5, "Q":0},
        {"W":1, "Q":0},
        {"N":1, "W":2, "Q":0},
        {"W":2, "S":1, "Q":0}]

loc=1
while True:
    availableExits=""
    for direction in exits[loc].keys(): # Not concise code
        availableExits+=direction+", "  # concise code.

    print(locations[loc])

    if loc==0:
        break

    direction=input("Available exits are " + availableExits).upper()
    print()
    if direction in exits[loc]:
        loc=exits[loc][direction] # <- 
    else:
        print("You cannot go in that direction")
