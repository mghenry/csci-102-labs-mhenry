#   Mary Henry
#   ​CSCI 102 – Section G
#   Week 3 - Lab B - Three Siblings
#   References: none
#   Time: 20 minutes

print('Input a positive number for the siblings to consider:')
number = int(input('NUMBER>'))

if (number % 2 != 0):
    print('OUTPUT Jimmy')
if (number <= 100) and (number >= 10):
    print('OUTPUT Jared')
if (number >= 10) and (number == 15 or 17 or 24 or 26 or 33 or 35 or 42 or 44 or 51 or 53 or 60 or 62 or 71 or 80):
    print('OUTPUT Josephine')
