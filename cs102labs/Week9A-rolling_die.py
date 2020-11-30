#   Maggie Henry
#   CSCI 102 – Section G
#   Week 9 - Lab A - Rolling a Die
#   References: None
#   Time: 20 minutes

from random import seed
from random import randint

print('Input the number of rolls to make:')
roll_times = int(input('NUMBER>'))
print('Input the seed for the random number generator:')
seed = int(input('SEED>'))

#seed(seed)
rolls = []

for i in range (roll_times):
    roll_num = randint(1, 6)
    rolls.append(roll_num)

print('Your ', roll_times, 'rolls follow:')

for i in range(len(rolls) ):
    print('OUTPUT ', i + 1, 'occured ', rolls[i], 'times.')

print(rolls)
