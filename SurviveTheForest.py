import random

#introduction
print("You wake up alone in a dark and scary forest. Try to make it out alive! You start out with 100% health.")

space = []
description = {
    1 : "You received 5 damage.",
    2 : "You received 10 damage.",
    3 : "You received 15 damage.",
    4 : "You received 20 damage.",
    5 : "You received 25 damage.",
    6 : "You received 30 damage."}

#print(description[1])

health = 100

#While health != 0 and sum(space) < 20:
for n in range(5):
    roll = input("To roll the die, press ENTER.")
    die = random.randint(1,6)
    print(f"You rolled a {die}.")
    space.append(die)
    #print(space)

    if sum(space) == 1:
        print(description[1])
    elif sum(space) == 2:
        print(description[2])
    elif sum(space) == 3:
        print(description[3])
    elif sum(space) == 4:
        print(description[4])
    elif sum(space) == 5:
        print(description[5])
    elif sum(space) == 6:
        print(description[6])
    else:
        print("ayo")