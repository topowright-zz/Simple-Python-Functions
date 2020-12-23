import random
#start = input('Press the Enter key to start:')

p1_total = 0


print(p1_total)

def turn(player):
    #Check our score
    print("The players total is : " + str(player))
    #start_roll = input('Press any key to roll:')
    roll = random.randrange(1,6)
    print("You rolled a:  " + str(roll))
    player = player + roll
    print("The new total is: " + str(player))
    return player


    # Roll Dice

    # Place fraction on the hexagon

possible_turns = 6
count = 0 
while count < possible_turns: 
    turns = turn(p1_total)
    count = count + 1
    print("   " +str(turns))
    p1_total = p1_total + turns
    print("Player now has :" + str(p1_total))
    print(count)
