#   Maggie Henry
#   ​CSCI 102 – Section G
#   Week 5 - Lab A - ASCII Carpet
#   References: no one
#   Time: 20 minutes

print('Input the dimensions for the rug and the character to print:')
width = int(input('WIDTH>'))
height = int(input('HEIGHT>'))
character = str(input('CHARACTER>'))

print('A ', width, 'x', height, 'rug with character', character, 'will look like:')

first_line = ''
for i in range(width):
    first_line = first_line + ' ' + character

for i in range(height):
    print('OUTPUT', first_line)

    
