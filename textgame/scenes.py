import enemy
import items

# basic scene class
class Scene(object):

    def enter(self):
        """The method that is used to enter a scene."""
        print("This scene isn't made yet.")

# class that ends the game
class Death(Scene):

    def enter(self):
        print('You are dead!')

#commented out scenes will be added later

class Tavern(Scene):

    def __init__(self):
        #these track if a player has visited certain people in game
        self.bar_visited = False
        self.strange_man_visited = False

    #This method decides what to do when offered an ale
    def bar_tend(self, choice, character):
        if choice == '1':
            if character.coins > 1:
                if character.coins > 0:
                    print('You buy an ale for 1 coin, and return to the tavern.')
                    character.coins -= 1
                    print(f"You have {character.coins} coins left")
                    return 'tavern'
                else:
                    print('You get caught trying to steal the barkeepers ale, he stabs you in the jugular.')
                    return 'death'
            else:
                print("You can't afford the ale, so you return the the tavern.")
                return 'tavern'
        elif choice == '2':
            print("You return to the tavern.")
            return 'tavern'

    #method that is used to enter the scene
    def enter(self, character):
        print("You enter the Tavern. To your left is a trader who is")
        print("sitting alone in the corner. Straight ahead, there is the bar. To")
        print("your right there is a strange man, staring at you. Do you:")
        print("1. Go to the bar. \n2. Talk to the trader \n3. Talk to the strange man\n4. Leave the tavern.")
        user_input = input('> ')

        if user_input == '1':
            #If the user hasn't visited the bar before, give different dialogue.
            if self.bar_visited == False:
                self.bar_visited = True
                print("The bartender sees you coming and offers you some ale...")
                print("And some advice. \"Avoid the strange man over there!\"")
                print("Do you:\n1. Buy an ale.\n2. Go back to the tavern.")
                choice = input('> ')
                return self.bar_tend(choice, character)

            else:
                print("The bartender welcomes you back and offers you some ale!")
                print("Do you:\n1. Buy an ale.\n2. Go back to the tavern.")
                choice = input('> ')
                return self.bar_tend(choice, character)

        elif user_input == '2':
            print("As you approch the trader he says, \"If you wish to see my wares, meet me at my wagon!\"")
            print("You make your way back to tavern.")
            return 'tavern'

        elif user_input == '3':
            #If the user hasn't approached the stranger man before, give different dialogue.
            if self.strange_man_visited == False:
                self.strange_man_visited = True
                print("As you approach the strange man he gazes on you with curious eyes. He says to you:")
                print("You look like just the person I was looking for. Let me ask you a question...")
                print("Would you like to have enough gold to buy whatever you heart desired?")
                print("Well if you're interested, I can tell you where you might be able to find some. For a price.")
                print("For 3 gold, I'll tell you where the treasure is and how to reach it.")
                print("Do you:\n1. Give the strange man the 3 gold.\n2. Decline and return to the tavern.")
                choice = input('> ')

                if choice == '1':
                    if character.coins >= 3:
                        character.coins -= 3
                        print("You give the strange man 3 gold. He tells you: ")
                        print(f"You have {character.coins} coins left")
                        print("The treasure can be found in the Imbued Ruins Treasure room, the chest is locked.")
                        print("But I know the combination is 3, 4, 5. There's also another chest in the Ancient Mines ")
                        print("Treasure room, and that ones combination is 7, 6, 5.")
                        print("You take this information and return to the tavern")
                        return 'tavern'
                    else:
                        print("The strange man catches you trying to scam him, and stabs you.")
                        return 'death'

                elif choice == '2':
                    print("You politely decline and return to the tavern")
                    return 'tavern'

                else:
                    print("You accidentally trip and break every bone in your body, and then get impaled by a sword.")
                    return 'death'

            else:
                print("The strange man asks how it's been going. You reply 'Good' and head back to the tavern.")
                return 'tavern'

        elif user_input == '4':
            return 'town_center'

        else:
            print("Unforunately the ceiling collapses and lands directly on your head.")
            return 'death'



class TownCenter(Scene):

    def enter(self, character):
        print("In the town center you see a tavern, a general store, a trader's wagon, and a way out of town.")
        print("Do you go to:\n1. Tavern\n2. General Store\n3. Trader's Wagon\n4. Head out of town.")
        user_choice = input('> ')

        if user_choice == '1':
            print('You head towards the tavern.')
            return 'tavern'
        elif user_choice == '2':
            print('You head towards the general store.')
            return 'general_store'
        elif user_choice == '3':
            print('You head towards the trader wagon.')
            return 'trader_wagon'
        elif user_choice == '4':
            print('You head out of town on the road.')
            return 'road_out_of_town'
        else:
            print('While trying to make up your mind you get stabbed by a horse. What a shame.')
            return 'death'

class GeneralStore(Scene):

    def enter(self, character):
        print("As you enter the general store, the sign says:")
        print("Daggers: 6 coins. Swords: 6 coins. Health potion: 3 coins.")
        print("The dagger seems to be fast, but do less damage, where-as the sword is slow but does far greater damage.")
        print("The health potions looks like it'll heal you 30hp.")
        print("Would you like to buy anyting?\n1. Yes\n2. No")
        user_input = input('> ')

        if user_input == '1':
            print("What would you like to buy?\n1. Sword\n2. Dagger\n3. Health Potion")
            choice = input('> ')

            if choice == '1':
                #checks if the character has sufficient coins to purchase the item
                if character.coins > 5:
                    #if they do have enough, buy the item and remove coins. then add the sword to the characters inventory.
                    character.coins -= 5
                    print(f"You purchase the sword. You have {character.coins} coins left.")
                    character.inventory['sword'] = items.Sword()
                    print("You walk back to the sign to see if there's anything else you want.")
                    return 'general_store'
                else:
                    print("Sorry, you can't afford that!")
                    return 'general_store'
            elif choice == '2':
                if character.coins > 5:
                    character.coins -= 5
                    print(f"You purchase the dagger. You have {character.coins} coins left.")
                    character.inventory['dagger'] = items.Dagger()
                    print("You walk back to the sign to see if there's anything else you want.")
                    return 'general_store'
                else:
                    print("Sorry, you can't afford that!")
                    return 'general_store'
            elif choice == '3':
                if character.coins > 2:
                    character.coin -= 2
                    print(f"You purchase the health potion. You have {character.coins} coins left.")
                    character.inventory['health-potion'] = items.HealthPotion()
                    print("You walk back to the sign to see if there's anything else you want.")
                    return 'general_store'
                else:
                    print("Sorry, you can't afford that!")
                    return 'general_store'
            else:
                print("Not a valid choice, you head back to try again.")
                return 'general_store'

        elif user_input == '2':
            print("You head back out into the town center.")
            return 'town_center'

        else:
            print('The shop owner catches you loitering and kicks you out into the town center.')
            return 'town_center'




class TraderWagon(Scene):

    def enter(self, character):
        print('You approach the trader at his wagon...')
        print("He says: \"Ahhh you look like you could use something like this my friend.\"")
        print("The trader pulls out a bow.")
        print("\"It isn't much use in a fight, but it can be used to grapple things from a distance! Only 5 gold.\"")
        print("Do you:\n1. Purchase the bow.\n2. Head back to the town center.")
        user_input = input('> ')

        if user_input == '1':
            if character.coins > 4:
                character.coins -= 5
                print(f"You purchase the bow. You have {character.coins} coins remaining.")
                character.inventory['bow'] = items.Bow()
                print('You head back out into the town center.')
                return 'town_center'
            else:
                print("You don't have enough to buy that! You head back out into the town center.")
                return 'town_center'
        elif user_input == '2':
            print("You have no interest in the bow, and head back out into the town center.")
            return 'town_center'
        else:
            print('You fall alseep making up your mind and somehow end up back at the town center.')
            return 'town_center'


class RoadOutOfTown(Scene):

    def enter(self, character):
        print('As you head down the road out of town you come across two trails.')
        print('The one to the left has a sign that reads "Gloomy Forest"...')
        print('The one of the right has a sign that reads "Somber Mountains".')
        print("Do you go:\n1. Left\n2. Right\n3. Back to town")
        user_input =  input('> ')

        if user_input == '1':
            print("You enter the Gloomy Forest.")
            return 'gloomy_forest'
        elif user_input == '2':
            print("You enter the Somber Mountains.")
            return 'somber_mountains'
        elif user_input == '3':
            print("You head back to the town center.")
            return 'town_center'

#From the Gloomy Forest, you get to explore the Imbued Ruins
class GloomyForest(Scene):

    def __init__(self):
        pass

    def enter(self, character):
        print("As you're walking through the forest, the heavy air makes it feel like you can't breath.")
        print("The weeds and vines seem to grab at your ankles as you trudge through the thick brush.")
        print("It's as if the place itself is evil and has every intention of murdering you.")
        print("You hear a branch snap in the distance and leaves rustling, as something explodes out of the darkness.")
        print("There's 3 Goblins, each one somehow uglier than the last.")
