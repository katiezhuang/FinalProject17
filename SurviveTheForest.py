#import random

#introduction
print("You wake up alone in a dark and scary forest. Try to make it out alive! You start out with 100% health and 10 stamina.")

name = input("What is your name?").lower

print(f"Hey {name}! Let's get started with our boardgame. There are twenty spaces to land on.")
print(f"When you land on a space, an event will occur and you will have to face the consequences!")
print(f"Each time you roll, you will lose 1 stamina. Run out of stamina or reach 0% health and you lose. Good luck {name}!")

#empty list to decide position
# space = []
# #description of every position
# description = {
#     1 : "You received 5 damage.",
#     2 : "You received 10 damage.",
#     3 : "You received 15 damage.",
#     4 : "You received 20 damage.",
#     5 : "You received 25 damage.",
#     6 : "You received 30 damage.",}

# #print(description[1])


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