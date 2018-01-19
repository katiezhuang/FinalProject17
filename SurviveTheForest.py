import random
import time

#introduction
print("You wake up alone in a dark and scary forest. Try to make it out alive! You start out with 100% health and 10 stamina.")

#take user input for name
name = input("What is your name? ")

#instructions for game
print(f"Hey {name}! Let's get started with our boardgame. There are twenty spaces to land on.")
time.sleep(3)
print(f"When you land on a space, an event will occur and you will have to face the consequences!")
time.sleep(3)
print(f"Each time you roll, you will lose 1 stamina. Run out of stamina or reach 0% health and you lose.")
time.sleep(3)
print(f"Whenever you want to check your stats, type STATUS. Good luck {name}!")
time.sleep(3)

#Spot class to organize each spot to land on
class Spot(object):

    def __init__(self, health, description = '', loot = ''):
        self.health = health
        self.description = description
        self.objects = loot

#Player class to define status of Player throughout the game
class Player(object):

    def __init__(self):
        self.location = 0
        self.health = 100
        self.stamina = 10
        self.spaces = [Spot(0), Spot(1, "K", "berries"), Spot(-5, "A", "poop"), Spot(2, "T", "dogs"), Spot(-2, "I", "butterflies"),
        Spot(-10, "E"), Spot(-20, "I", "kittens"),
        Spot(5, "S", "berries"), Spot(-10, "A", "box"), Spot(-5, "M", "trees"), Spot(-15, "A"), Spot(-20, "Z"),
        Spot(-45, "I"), Spot(-30, "N"), Spot(-40, "G"), Spot(-9, "R"),
        Spot(-15, "E"), Spot(-15, "A"), Spot(-15, "L"), Spot(-15, "L"), Spot(-15, "Y")]
        self.current_space = self.spaces[0]
        self.inventory = []

    def loser(self):
        if self.health <= 0 or self.stamina == 0:
            return True
        else:
            return False

    def winner(self):
        if self.location > 20 and self.health > 0:
            return True
        else:
            return False

    def move(self, move_by):
        self.location += move_by
        if self.location <= 20:
            self.current_space = self.spaces[self.location]
        else:
            print("LOSER")


    def resolve(self):
        print(self.current_space.description)

        self.health += self.current_space.health
        print(f"Player's health is now {self.health}.")

        self.stamina -= 1
        print(f"Player's stamina is now {self.stamina}.")

        if len(self.current_space.objects) > 0:
            self.inventory.append(self.current_space.objects)
            print(f"Player added {self.current_space.objects} to their inventory and now has {self.inventory}")
        else:
            print("There is nothing to add to your inventory.")

        if self.loser():
            if self.health <= 0:
                print("GAME OVER. You've reached 0% health.")
            if self.stamina == 0:
                print("GAME OVER. You've lost all of your stamina!")
        elif self.winner():
            print(f"Congratulations {name}! You have reached the end and won the game! You have played SURVIVETHEFOREST.")

    def status(self):
        print(f"{name} is at {self.health}% health.")
        print(f"{name} is at {self.stamina} stamina.")


#create an object of the Player class
a = Player()

#empty list to keep track of number of rolls
space = []

#description of every position
# description = {
#     1 : "You received 5 damage.",
#     2 : "You received 10 damage.",
#     3 : "You received 15 damage.",
#     4 : "You received 20 damage.",
#     5 : "You received 25 damage.",
#     6 : "You received 30 damage.",}

#print(description[1])

#while loop to prompt player to roll the die and move
while not a.loser() and not a.winner():

    roll = input("To roll the die, press ENTER.")

    die = random.randint(1,6)

    print(f"You rolled a {die}.")

    space.append(die)
    #print(space)

    a.move(die)

    a.resolve()

# class Player(object):
#     """
#     ATTRIBUTES
#     health
#     stamina
#     """

#     def __init__(self):
#         self.health = 100
#         self.stamina = 10
#         position = sum(space)

#     def move(self):
#         """called every time player moves on the board"""
#         self.health
#         self.stamina -= 1
#         if self.loser():
#             if self.health <= 0:
#                 print("GAME OVER. You've reached 0% health.")
#             if self.stamina == 0:
#                 print("GAME OVER. You've lost all of your stamina!")
#         elif self.winner():
#             print(f"Congratulations {name}! You have reached the end and won the game! You have played SURVIVETHEFOREST.")

#     def status(self):
#         print(f"{name} is at {self.health}% health.")
#         print(f"{name} is at {self.stamina} stamina.")

#     def loser(self):
#         if self.health <= 0 or self.stamina == 0:
#             return True
#         else:
#             return False

#     def winner(self):
#         if sum(space) > 20 and self.health > 0:
#             return True
#         else:
#             return False

# a = Player()

# #While not a.loser() and not a.winner(): and sum(space) <= 20:
# for n in range(5):
#     roll = input("To roll the die, press ENTER.")
#     die = random.randint(1,6)
#     print(f"You rolled a {die}.")
#     space.append(die)
#     #print(space)

#     position = sum(space)
#     if position == 1:
#         print(description[1])
#     elif position == 2:
#         print(description[2])
#     elif position == 3:
#         print(description[3])
#     elif position == 4:
#         print(description[4])
#     elif position == 5:
#         print(description[5])
#     elif position == 6:
#         print(description[6])
#     else:
#         print("ayo")