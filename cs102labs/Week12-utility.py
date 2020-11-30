#   Maggie Henry
#   CSCI 102 – Section G
#   Week 12 - Utility using Git and Incremental Development
#   References: www.geeksforgeeks.org, www.stackoverflow.com, zyBooks
#   Time: 1.5 hours


def load_file(some_file_name):
    file_to_read = open("some_file_name")
    file_list = file_to_read.readlines()
    file_to_read.close()
    return file_list

def update_string(string1, string2, integer):
    integer = int(integer)
    temp_string_front = string1[:integer]
    temp_string_back = string1[integer:]
    temp_string = temp_string_front + string2 + temp_string_back
    print('OUTPUT', temp_string)

def find_word_count(list_to_parse, string_to_find):
    count_num = 0
    for i in range(len(list_to_parse)):
        if list_to_parse[i-1] == string_to_find:
            count_num += 1
    return count_num

def score_finder(player_names, player_scores, name):
    for i in range(len(player_names)):
        if player_names[i-1] == name:
            index = i-1
        else:
            print('player not found')
    print('OUTPUT', name, 'got a score of', player_scores[index])

def union(list1, list2):
    new_list = list1 + list2
    return new_list

def intersect(list1, list2):
    same_elem = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                same_elem.append(list1[i])
    return same_elem

def not_in(list1, list2):
    added_list = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] != list2[j]:
                added_list.append(list1[i])
    for i in range(len(list2)):
        for j in range(len(added_list)):
            if list2[i] != added_list[j]:
                added_list.append(list2[i])
    return added_list

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
        
            
                
                
