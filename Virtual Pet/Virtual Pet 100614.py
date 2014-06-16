#Aaron Parker
#100614
#Virtual Pet

class Player:
    """A list of items the player possesses"""
    #Constructor
    def __init__(self):
        self.food = 5

    def items(self):
        print()
        print("Items in possession:")
        print("Pet food: {0}".format(self.food))
        print()


class VirtualPet:
    """A representation of a pet."""
    #Constructor - run automatically
    def __init__(self,name):
        
        #Basic stats
        self.name = name
        self.hunger = 100
        self.level = 1
        self.xp = 100
        
        #Combat stats
        self.hp = 100
        self.mp = 50
        self.pattack = 1
        self.mattack = 1
        self.speed = 2
        
        print("{0} rises from the ashes!".format(self.name))

    #Methods
    def pet_status(self):
        #prints details on pet
        print()
        print("Pet Stats:")
        print("Pet name = {0}".format(self.name))
        print("Pet hunger = {0}".format(self.hunger))
        print()


    def level_up(self):
        self.level = self.level + 1
        self.xp = 0
        self.hp = self.hp + 25
        self.mp = self.mp + 10
        self.pattack = self.pattack + 1
        self.mattack = self.mattack + 1
        self.speed = self.speed + 1
        print("**********LEVEL UP**********")
        print()
        print("You have advanced to level {0}!".format(self.level))
        print("{0}'s HP has increased from {1} to {2}!".format(self.name,self.hp-25,self.hp))
        print("{0}'s MP has increased from {1} to {2}!".format(self.name,self.mp-10,self.mp))
        print("Please choose which stat you wish to level from the list below.")
        print()
        
    def talk(self):
        #prints statement
        if self.hunger >= 5:
            print("Hi, im your virtual pet!")
            self.hunger = self.hunger - 5
        else:
            print("{0} cannot speak, it is too hungry. (hunger = {1})".format(self.name,self.hunger))
        
    
        


def display_menu():
    print()
    print("#####-MAIN MENU-#####")
    print("1.Make your pet speak")
    print("2.Check your pet's hunger status")
    print("0.View stats")
    print()

def level_up_options(pet_one):
    print()
    print("1. Physical Attack: {0} --> {1}".format(pet_one.pattack,pet_one.pattack + 1))
    print("2. Magical Attack: {0} --> {1}".format(pet_one.mattack,pet_one.mattack + 1))
    print("3. Speed: {0} --> {1}".format(pet_one.speed,pet_one.speed + 1))
    print()

def pet_name():
    #Asks the user to enter a valid name, and returns it.
    valid = False
    while not valid:
        name = input("Please enter a name for your pet: ")
        if name.isalpha() == True:
            valid = True
        else:
            print("Please enter a valid name, that is at least 1 letter long.")
            
    return name



def level_up_pet(pet_one):
    #Levels up the pet
    pet_one.level_up()
    level_up_options(pet_one)

    valid = False
    while not valid:
        stat_choice = int(input("Stat Choice: "))
        if stat_choice in range(1,4):
            valid = True
        else:
            print("Please make a valid stat choice.")

    if stat_choice == 1:
        pet_one.pattack = pet_one.pattack + 1
    elif stat_choice == 2:
        pet_one.mattack = pet_one.mattack + 1
    elif stat_choice == 3:
        pet_one.speed = pet_one.speed + 1


def hunger_status(playerstats,pet_one):
        #States Hunger value and asks if you wish to feed your pet
        print("Hunger is {0}.".format(pet_one.hunger))
        if playerstats.food <= 0:
            print("You cannot feed {0},as you have no food.".format(pet_one.name))
        if playerstats.food >0:
            valid = False
            while not valid:
                feed = input("Would you like to feed {0}[Y/N]? (amount of food = {1}) ".format(pet_one.name,playerstats.food))
                feed = feed[0].upper()
                if feed == "Y" or feed == "N":
                    valid = True
                else:
                    print("Please enter a valid choice.")
            if feed == "Y":
                pet_one.hunger = 100
                playerstats.food = playerstats.food - 1
                print("{0}'s health is restored to 100.".format(pet_one.name))
                print("You have {0} pet food left.".format(playerstats.food))
            else:
                print("You chose not to feed your pet.")
                
def main():
    playerstats = Player()
    name = pet_name()
    #Creates an instance of the class
    pet_one = VirtualPet(name)
    choice = 0

    while choice != ("q" or "Q"):
        xp_threshold = 100*pet_one.level
        if pet_one.xp >= xp_threshold:
            level_up_pet(pet_one)
        display_menu()
        print()
        choice = input("Please make your choice (or enter q to quit): ")
        print()
        if choice == "1":
            pet_one.talk()
        elif choice == "2":
            hunger_status(playerstats,pet_one)
        elif choice == "0":
            pet_one.pet_status()
            playerstats.items()
        elif choice == "q" or choice == "Q":
            print()
        else:
            print("Please enter a valid choice from the menu")
            print()


if __name__ == "__main__":
    main()
