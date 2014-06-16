#Aaron Parker
#160614
#Battle Pets

import random

class Grunt:

    #constructor
    def __init__(self):
        
        self._HP = random.randint(2,5)
        self._Attack = random.randint(1,3)
        self._Defense = random.randint(1,2)
        self._Speed = random.randint(1,3)

def main():
    for count in range(5):
        new_pet = Grunt()
        print(new_pet._HP)
        print(new_pet._Attack)
        print(new_pet._Defense)
        print(new_pet._Speed)

if __name__ == "__main__":
    main()
