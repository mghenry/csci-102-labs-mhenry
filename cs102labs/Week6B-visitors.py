#   Maggie Henry
#   ​CSCI 101 – Section G
#   Week 6 - Lab B - Unique Visitors
#   References: none
#   Time: 60 minutes

print('Enter the users seperated by commas:')

name_string = str(input('USERS>'))
last_index = 0
name_list = []
i = 0

for i in range(len(name_string)):
    if name_string[i] == ',':
        split_string = name_string[last_index:i]
        split_string = split_string.lower()
        name_list.append(split_string)
        last_index = i + 2
    

last_index = name_string.rindex(',')
last_name = name_string[last_index + 2:]
last_name = last_name.lower()
name_list.append(last_name)
    
count = 0

name_count = {}

for i in name_list:
    if i in name_count.keys():
        name_count[i] += 1
    else:
        name_count[i] = 1
        
print('You entered the following users:')
print('OUTPUT', name_list)
print('The unique users and their occurences are:')
print('OUTPUT', name_count)


