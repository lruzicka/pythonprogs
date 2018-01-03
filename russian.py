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
    trigger = drum[0]
    return(trigger)
        


slots = input("How many slots does your gun have?: ")
slots = int(slots)

bullets = input("How many bullets do you want to load?: ")
bullets = int(bullets)

if bullets < slots:
    input("Press the trigger!")

    drum = load(slots,bullets)
    drum = rotate(drum)
    result = shoot(drum)

    if result == 1:
        print("You die!")
    else:
        print("You survived!")
    
else:
    print("You are stupid, you cannot load so many bullets. You only have {} slots.".format(slots))
