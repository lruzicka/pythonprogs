from random import shuffle

def load(slots,bullets):
    """Load bullets into the drum for the game."""
    drum = []
    for bullet in range(0,bullets):
        drum.append(1)
     
    while slots > len(drum):
        drum.append(0)
    return(drum)

def rotate(drum):
    """Shuffles the bullets in the drum."""
    shuffle(drum)
    return(drum)

def shoot(drum):
    """Shoot and see"""
    trigger = drum.pop(0)
    drum.append(0)
    return(trigger)
        
#-------------------------------------------------------------------------------------------

print("Welcome to the game of courageous tsars. Take your gun and let's play!")

slots = input("How many slots does your gun have?: ")
slots = int(slots)

bullets = input("How many bullets do you want to load?: ")
bullets = int(bullets)

if bullets < slots:
    risk = True
    drum = load(slots, bullets)
    drum = rotate(drum)
    
    while risk == True:
        input("Press the trigger!")
        result = shoot(drum)
            
        if result != 1:
            print("You survived!")
            decision = input("Do you want to continue? (y/N): ")
            if decision == 'y':
                risk = True
                decision = input("Do you want to be a coward and rotate the drum again? (y/N): ")
                if decision == 'y':
                    drum = rotate(drum)
            else:
                    risk = False
                    print("You coward! Take your shitty pants out of this company!")
            
        else:
            print("You painted the walls with your brain!")
            risk = False
            
    
else:
    print("You are stupid, you cannot load so many bullets. You only have {} slots.".format(slots))
