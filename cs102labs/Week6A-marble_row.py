#   Maggie Henry
#   ​CSCI 101 – Section G
#   Week 6 - Lab A - Lost Marbles
#   References: none
#   Time: 30 minutes

print("Enter a string of X's and O's:")
marble_string = str(input('MARBLES>'))

marble_place = []
marble = "O"

for i in range(len(marble_string)):
    if marble_string[i] == marble:
        marble_place.append(i)
        
print('Your marbles are at the following indices:')
print('OUTPUT', marble_place)


                    
