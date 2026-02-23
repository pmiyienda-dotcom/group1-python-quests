direction = input("Are you going left or right: ")

if direction == "left":   
    activity = input("Will you swim or wait: ")
    if activity == "swim":
        print ("You found a treasure")
    else:
        print ("No treasure")
else:
    print ("You went right and got lost")
    