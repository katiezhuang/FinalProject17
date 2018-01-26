import random
import time


#introduction
print("You wake up alone in a dark and scary forest. Try to make it out alive! You start out with 100% health and 10 stamina.")

#take user input for name
name = input("What is your name? ")

#instructions for game
#delayed with import time
print(f"\nHey {name}! Let's get started with our boardgame. There are twenty spaces to land on.\n")

time.sleep(1)

print(f"When you land on a space, an event will occur and you will have to face the consequences!")

time.sleep(3)

print(f"Each time you roll, you will lose 1 stamina. Run out of stamina or reach 0% health and you lose.")

time.sleep(3)

print(f"Whenever you want to check your stats or inventory, type status before rolling. Good luck {name}!\n")

time.sleep(3)

#choose a game piece
piece_choices = """Bunny
Human
Ant
"""
ls_piece = ["Bunny", "Human", "Ant"]

print(piece_choices)

while True:
    game_piece = input("What game piece do you want? ").title()

    if game_piece in ls_piece:
        print(f"Great! You are now a {game_piece}!\n")
        break
    else:
        print(f"{game_piece} is not one of the choices! Choose again!\n")

#Spot class to organize each spot to land on
class Spot(object):

    def __init__(self, health, description = '', loot = ''):
        """Each spot on the board may or may not have a health, a description, and an object"""
        self.health = health
        self.description = description
        self.objects = loot

#Player class to define status of Player throughout the game
class Player(object):

    def __init__(self):
        """Player starts at location 0, with 100 health, and 10 stamina.
        Spaces is a list of spots to land on, each spot with its own parameters.
        The initial current space is the spot with index 0 in the list.
        The inventory of the player starts out as a blank list."""
        self.location = 0
        self.health = 100
        self.stamina = 10
        self.spaces = [Spot(0),
        Spot(0, f"You are now on space 1. {game_piece} walks deeper into the forest to find fresh and ripe berries on a nearby bush. {game_piece} eagerly bends down to pick some off.\n", "berries"),
        Spot(-5, f"You are now on space 2. {game_piece} trips on a pebble. {game_piece} looks up to find a gleaming sword.\n", "gleaming sword"),
        Spot(25, f"You are now on space 3. {game_piece} sees a squirrel and befriends it. The squirrel is now a great companion!\n", "squirrel"),
        Spot(-20, f"You are now on space 4. {game_piece} comes across a brown bear who is ready to eat. Some health was lost due to fear.\n"),
        Spot(-10, f"You are now on space 5. {game_piece} sees a bird and scares it away. You are a terrible person. 10% health was lost.\n"),
        Spot(-20, f"You are now on space 6. Yikes. It looks like {game_piece} bumped into a forest troll. 20% health was lost.\n",),
        Spot(5, f"You are now on space 7. {game_piece} finds some mushrooms on the side of a giant tree and decides to pick it up.", "mushrooms"),
        Spot(-10, f"You are now on space 8. {game_piece} got hangry!"),
        Spot(-5, f"You are now on space 9. {game_piece} stepped on a baby porcupine. Ouch! {game_piece} found a giant branch.", "branch"),
        Spot(-15, f"You are now on space 10. {game_piece} is sooooooo tired now for some reason."),
        Spot(-20, f"You are now on space 11. It looks like {game_piece} passed that tree fives time now. {game_piece} got lost and is now on space 6."),
        Spot(-45, f"You are now on space 12. {game_piece} found a fairy! In exchange for 30% of your health, the forest fairy returned 1 stamina point and some medicinal herbs.", "medicinal herbs"),
        Spot(-30, f"You are now on space 13. {game_piece} was not careful and fell into a hole. That sucks! {game_piece} is now severly injured."),
        Spot(-40, f"You are now on space 14. {game_piece} got robbed by that sneaky fox and got the first item in your inventory stolen! The fox left behind a piece of meat.", "meat"),
        Spot(-9, f"You are now on space 15. {game_piece} trips over a shiny object. What is that? Oh, it's a coin!", "coin"),
        Spot(-15, f"You are now on space 16. {game_piece} took a nap and restored 1 stamina. But, {game_piece} did not sleep too comfortably on the forest ground. Some health was lost."),
        Spot(-15, f"You are now on space 17. {game_piece} found a coin in a tree. Climbing it ruffled {game_piece} up a bit. Some health was lost.", "coin2"),
        Spot(-15, f"You are now on space 18. {game_piece} meets a closet wizard who hides in the forest."),
        Spot(-15, f"You are now on space 19. {game_piece} meets a forest troll."),
        Spot(-15, f"You are now on space 20. {game_piece} suddenly bumps into a strange man with a long beard. He is angry that {game_piece} landed on his space and tells {game_piece} to go back. Before you realize it, {game_piece} is back at space 1.")]
        self.current_space = self.spaces[0]
        self.inventory = []

    #if health is less than or equal to 0 or stamina reaches 0, the player is loser.
    #Otherwise, they are not.
    def loser(self):
        if self.health <= 0 or self.stamina == 0:
            return True
        else:
            return False

    #if the location of the player is more than 20, the player is a winner.
    #Otherwise, they are not.
    def winner(self):
        if self.location > 20:
            return True
        else:
            return False

    #when the player object moves, the location is increased by that amount.
    #if the location of the player is less than or equal to 20,
    #the location becomes the index of the spaces list, specifying the Spot as the current space.
    def move(self, move_by):
        self.location += move_by
        if self.location <= 20:
            self.current_space = self.spaces[self.location]
        else:
            print(f"You are now on space {self.location}.")


    #prints the description of the space, the updated health, stamina, and inventory.
    #if the player is a loser or winner, the game is over.
    #player can check for status at any time.
    def resolve(self):
        time.sleep(2)

        if self.location <= 20:
            print(self.current_space.description)

        time.sleep(1)

        self.health += self.current_space.health
        print(f"{game_piece}'s health is now {self.health}.")

        time.sleep(1)

        self.stamina -= 1
        print(f"{game_piece}'s stamina is now {self.stamina}.")

        time.sleep(1)

        if len(self.current_space.objects) > 0:
            self.inventory.append(self.current_space.objects)
            time.sleep(2)
            print(f"\nPlayer added {self.current_space.objects} to their inventory and now has {self.inventory}.\n")
        else:
            time.sleep(2)
            print("\nThere is nothing to add to your inventory.\n")

        if self.loser():
            if self.health <= 0:
                print("GAME OVER. You've reached 0% health.")
            if self.stamina == 0:
                print("GAME OVER. You've lost all of your stamina!")
        elif self.winner():
            print(f"Congratulations {name}! You have reached the end and won the game! You have played SURVIVETHEFOREST.")

    #prints your status: health, stamina, location, inventory
    def status(self):
        print(f"{game_piece} is at {self.health}% health.")
        print(f"{game_piece} is at {self.stamina} stamina.")
        print(f"{game_piece} is on Space {self.location}.")
        if len(self.inventory) == 0:
            print("There is nothing in your inventory.")
        else:
            print(f"Inventory contains {self.inventory}.")

    #more prompts to player after landing on each spot
    def other(self):
        if self.current_space == self.spaces[1]:
            while True:
                eat = input("Would you like to eat your berries? y/n ").lower()
                if eat == "y":
                    print("Delicious! Your health increased by 5%.")
                    self.inventory.remove("berries")
                    self.health += 5
                    self.status()
                    break
                elif eat == "n":
                    print("Ok! If you ever want to eat your berries, type berries.")
                    break
                else:
                    print("That's not a valid answer. Try again!")
        elif self.current_space == self.spaces[2]:
            print("Type gleaming sword when you want to activate it.")
        elif self.current_space == self.spaces[3]:
            while True:
                squirrely = input("Would you like to talk to your squirrel? y/n ").lower()
                if squirrely == "y":
                    print('Squirrel says "Well hi!"')
                    break
                elif squirrely == "n":
                    print("Ok! If you ever want to talk to your squirrel companion, type squirrel.")
                    break
                else:
                    print("That's not a valid answer. Try again!")
        elif self.current_space == self.spaces[4]:
            while True:
                bear_choice = input("Do you want to \na) fight the bear\nb) feed the bear\nc) try to befriend the bear?\n").lower()
                if bear_choice == "a":
                    if "gleaming sword" in self.inventory:
                        print("You tried to fight the bear with your gleaming sword.")
                        print("...it was successful! The bear was slayed.")
                        break
                    else:
                        print("Sorry! You have nothing in your inventory to fight the bear with. Pick another choice!")
                elif bear_choice == "b":
                    if "berries" in self.inventory:
                        print("You chose to feed the bear with the berries in your inventory.")
                        self.inventory.remove("berries")
                        break
                    else:
                        print("Sorry! You don't have anything in your inventory to feed the bear. Choose another option!")
                elif bear_choice == "c":
                    print("Uh oh. I don't think it wants to be your friend. You lose 10% health.")
                    self.health -= 10
                    break
                else:
                    print("That's not a valid answer. Try again!")
        elif self.current_space == self.spaces[6]:
            while True:
                troll_answer = "lighthouse"
                troll_question = input(f'The troll decides that you have to answer his riddle correctly for {game_piece} to pass. He asks, "What type of house weighs the least?".').lower()
                if troll_question == troll_answer:
                    print(f"You answered the riddle correctly! It was {troll_answer}.")
                    break
                else:
                    print("Try Again! You lost 5% health.")
                    self.health -= 5
        elif self.current_space == self.spaces[7]:
            while True:
                shrooms = input("Would you like to eat your mushrooms? y/n ").lower()
                if shrooms == "y":
                    print("Yucky! They taste bad and they're poisonous! SO not your day.")
                    self.inventory.remove("mushrooms")
                    self.health -= 20
                    self.status()
                    break
                elif shrooms == "n":
                    print("Ok! If you ever want to eat your mushrooms, type mushrooms.")
                    break
                else:
                    print("That's not a valid answer. Try again!")
        elif self.current_space == self.spaces[8]:
            while True:
                self.status()
                hungry = input("Would your like to eat something? y/n ").lower()
                if hungry == "y":
                    if "berries" in self.inventory or "mushrooms" in self.inventory:
                        while True:
                            hangry = input("What would you like to eat?").lower
                            if hangry == "berries":
                                self.inventory.remove("berries")
                                break
                            elif hangry == "mushrooms":
                                self.inventory.remove("mushrooms")
                                print("Those mushrooms were poisonous! Some health was lost.")
                                self.health -= 5
                                break
                            else:
                                print(f"You can't eat that! Try again")
                    else:
                        print("Sorry. There is no food in your inventory. Some health was lost.")
                        self.health -= 10
                        break
                elif hungry == "n":
                    print("But you're really starving! Some health was lost.")
                    self.health -= 10
                    break
                else:
                    print("That's not a valid answer. Try again!")
        elif self.current_space == self.spaces[10]:
            tired = input("Would your like to eat something? y/n ").lower()
            if tired == "y":
                if "berries" in self.inventory or "mushrooms" in self.inventory:
                    while True:
                        yum = input("What would you like to eat? mushrooms or berries(hint: they have to be in your inventory) ").lower()
                        print(yum)
                        if yum == "berries":
                            if "berries" in self.inventory:
                                self.inventory.remove("berries")
                                break
                            else:
                                print("You don't have any berries!")
                        elif yum == "mushrooms":
                            if "mushrooms" in self.inventory:
                                self.inventory.remove("mushrooms")
                                print("Those mushrooms were poisonous! Some health was lost.")
                                self.health -= 5
                                break
                            else:
                                print("You don't have any mushrooms!")
                        else:
                            print(f"You can't eat that! Try again")
                else:
                    print("Sorry. There is no food in your inventory. Some health was lost.")
                    self.health -= 10
            elif tired == "n":
                if "branch" in self.inventory:
                    while True:
                        stick = input("Would you like to use your branch as a cane? y/n ").lower()
                        if stick == "y":
                            print("Great! You're not so tired anymore!")
                            self.health += 5
                            break
                        elif stick == "n":
                            print("Well, ok then. Then I don't think there is any use to it anymore.")
                            self.inventory.remove("branch")
                            break
                        else:
                            print("That's not a valid answer!")
                #else:
                    #print("----------------")
            else:
                print("That's not a valid answer. Try again!")
        elif self.current_space == self.spaces[11]:
            self.move(-5)
        elif self.current_space == self.spaces[12]:
            self.health -= 30
            self.stamina += 1


            inputCheck = 0
            while inputCheck == 0:
                herby = input("Would you like to eat your medicinal herbs? y/n ").lower()
                if herby == "y":
                    print("Wowie! Your health increased by 5%.")
                    self.inventory.remove("medicinal herbs")
                    self.health += 5
                    self.status()
                    inputCheck = 1
                elif herby == "n":
                    print("Ok! If you ever want to eat your medicinal herbs, type medicinal herbs.")
                    inputCheck = 1
                else:
                    print("That's not a valid answer. Try again!")

            # while True:
            #     herby = input("Would you like to eat your medicinal herbs? y/n ").lower()
            #     print(herby)
            #     if herby == "y":
            #         print("Wowie! Your health increased by 5%.")
            #         self.inventory.remove("medicinal herbs")
            #         self.health += 5
            #         self.status()

            #     elif herby == "n":
            #         print("Ok! If you ever want to eat your medicinal herbs, type medicinal herbs.")
            #         break
            #     else:
            #         print("That's not a valid answer. Try again!")

        elif self.current_space == self.spaces[13]:
            if "medicinal herbs" in self.inventory:
                while True:
                    herby2 = input("Would you like to eat your medicinal herbs? y/n ").lower()
                    if herby2 == "y":
                        print("Wowie! Your health increased by 5%.")
                        self.inventory.remove("medicinal herbs")
                        self.health += 5
                        self.status()
                    elif herby2 == "n":
                        print("Ok! If you ever want to eat your medicinal herbs, type medicinal herbs.")
                    else:
                        print("That's not a valid answer. Try again!")
            #else:
                #print("-------------------------------")
        elif self.current_space == self.spaces[14]:
            if len(self.inventory) == 1:
                print("Oh. Actually, there is nothing in your inventory to steal.")
            else:
                self.inventory.remove(self.inventory[0])
        elif self.current_space == self.spaces[15]:
            print("Type coin when you want to activate it.")
        elif self.current_space == self.spaces[16]:
            self.stamina += 1
        elif self.current_space == self.spaces[17]:
            print("Type coin2 when you want to activate it.")
        elif self.current_space == self.spaces[18]:
            while True:
                trivia = input('The wizard wants to test your knowledge on the outside world. He asks you, "In which US state is John F Kennedy buried?"\n\nIs it:\na) Massachusetts\nb) Virginia\nc) Texas\nd) California\n(hint: if you have any coins in your inventory, you can give it to the wizard for a free answer!)').lower()
                if trivia == "b":
                    print("That's correct! You may move on.")
                    break
                elif trivia == "coin" or trivia == "coin2":
                    print("The wizard takes your coin and tells you that the correct answer is b.")
                else:
                    print("Hmm.. That is not the correct answer. Try Again?")
                    self.health -= 5
        elif self.current_space == self.spaces[19]:
            while True:
                troll_answer2 = "candle"
                troll_question2 = input(f'The troll decides that you have to answer his riddle correctly for {game_piece} to pass. He asks, "I am tall when I am young and short when I am old. What am I?".\n(hint: If you have a coin, type coin or coin2 to pay the troll to let you pass!)').lower()
                if troll_question2 == "candle":
                    print(f"You answered the riddle correctly! It was {troll_answer2}.")
                    break
                elif troll_question2 == "coin":
                    if "coin" in self.inventory:
                        self.inventory.remove("coin")
                        print("The troll takes your coin and tells you that the correct answer is candle.")
                    else:
                        print("You don't have a coin to spend!")
                elif troll_question2 == "coin2":
                    if "coin2" in self.inventory:
                        self.inventory.remove("coin2")
                        print("The troll takes your coin and tells you that the correct answer is candle.")
                    else:
                        print("You don't have coin2 to spend!")
                else:
                    print("That is not the correct answer. You lost 5% health.")
                    self.health -= 5
        elif self.current_space == self.spaces[20]:
            self.move(-19)
        else:
            print("")

#create an object of the Player class
a = Player()

#empty list to keep track of number of rolls
space = []

#while loop to prompt player to roll the die and move
while not a.loser() and not a.winner():
    while True:
        time.sleep(2)
        print("---------------------------------------------------------------------")
        roll = input("To roll the die, type roll. ")
        die = random.randint(1,6)

        if roll == "status":
            a.status()
            break
        elif roll == "berries":
            if "berries" in a.inventory:
                print("Delicious! Your health increased by 5%.")
                a.inventory.remove("berries")
                a.health += 5
                a.status()
                break
            else:
                print("You don't have berries in your inventory.")
                break
        elif roll == "gleaming sword":
            if "gleaming sword" in a.inventory:
                print("You don't need to use your gleaming sword right now!")
                break
            else:
                print("You don't have a gleaming sword in your inventory.")
                break
        elif roll == "squirrel":
            if "squirrel" in a.inventory:
                chat = random.randint(1,10)
                if chat == 1:
                    print("The forest is so scary!")
                elif chat == 2:
                    print("I NEED Nuts.")
                elif chat == 3:
                    print("Oh mAN. Can we takee a breeeak noww???")
                elif chat == 4:
                    print("I'm bored. Play with meeeee.")
                elif chat == 5:
                    print("You can talk to me anytime!")
                elif chat == 6:
                    print("The greatest gift of life is friendship, and I have received it.")
                elif chat == 7:
                    print("Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.")
                elif chat == 8:
                    print("Life isn't about finding yourself. Life is about creating yourself.")
                elif chat == 9:
                    print("Be happy for this moment. This moment is your life.")
                elif chat == 10:
                    print("Life is really simple, but we insist on making it complicated.")
            else:
                print("You don't have a squirrel in your inventory.")
                break
        elif roll == "mushrooms":
            if "mushrooms" in a.inventory:
                print("Oh no! Those were poisonous mushrooms. Your health decreased by 10%.")
                a.inventory.remove("berries")
                a.health -= 10
                a.status()
                break
            else:
                print("You don't have mushrooms in your inventory.")
                break
        elif roll == "branch":
            if "branch" in a.inventory:
                print("You don't really need it right now.")
                break
            else:
                print("You don't have a branch in your inventory.")
                break
        elif roll == "medicinal herbs":
            if "medicinal herbs" in a.inventory:
                print("Nice! Your health increased by 20%.")
                a.inventory.remove("medicinal herbs")
                a.health += 20
                a.status()
                break
            else:
                print("You don't have medicinal herbs in your inventory.")
                break
        elif roll == "meat":
            if "meat" in a.inventory:
                print("Delicious! Your health increased by 10%.")
                a.inventory.remove("meat")
                a.health += 10
                a.status()
                break
            else:
                print("You don't have meat in your inventory.")
                break
        elif roll == "coin":
            if "coin" in a.inventory:
                print("Yey! You're richh. Your stamina increased")
                a.inventory.remove("coin")
                a.stamina += 1
                a.status()
                break
            else:
                print("You don't have coin in your inventory.")
                break
        elif roll == "coin2":
            if "coin2" in a.inventory:
                print("Sweet! You're rich! Your stamina increased.")
                a.inventory.remove("coin2")
                a.stamina += 2
                a.status()
                break
            else:
                print("You don't have coin2 in your inventory.")
                break
        elif roll == "roll":
            print(f"You rolled a {die}.\n")
            space.append(die)
            #print(space)

            a.move(die)

            a.resolve()

            if a.location <= 20 and a.health > 0 and a.stamina > 0:
                a.other()
            break

        else:
            print("type roll to roll, status to see your stats, and any object in your inventory to activate it.")















