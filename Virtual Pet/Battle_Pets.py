#Aaron Parker
#160614
#Battle Pets

import random

class Grunt:

    #constructor
    def __init__(self):
        
        self.HP = random.randint(2,5)
        self.Attack = random.randint(1,3)
        self.Defense = random.randint(1,2)
        self.Speed = random.randint(1,3)

    #def attack(self,defender):
    def stats(self):
        print()
        print("HP: {0}".format(self.HP))
        print("Attack: {0}".format(self.Attack))
        print("Defense: {0}".format(self.Defense))
        print("Speed: {0}".format(self.Speed))

        


def display_battle_menu():
    print()
    print("1. Attack")
    print()
    print("2. Defend & Recover")
    print()
    print("3. View Pet stats")
    print()
    print("0. Forfeit battle")
    print()
    print("What will you do?")


def battle(new_pet):
    opponent = Grunt()
    forfeit_battle = False
    
    while opponent.HP != 0 or while new_pet.HP != 0 or while forfeit_battle != True :
        
        display_battle_menu()

        valid = False
        while not valid:
            action = int(input("Action: "))
            if action in range(0,4):
                valid = True
            else:
                print("You cannot do that!")
        
        if action == 1:
            new_pet.attack(opponent)
            print()
            opponent.move(new_pet)
        elif action == 2:
            new_pet.recover()
            print()
            opponent.move(new_pet)
        elif action == 3:
            new_pet.stats()
            print()
        elif action == 0:
            forfeit()
            print()
            foreit_battle = True

    
    

def main():
    for count in range(5):
        new_pet = Grunt()
        battle(new_pet)
        

if __name__ == "__main__":
    main()
