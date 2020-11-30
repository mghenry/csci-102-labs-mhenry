#   Maggie Henry
#   CSCI 102 – Section G
#   Week 12 - Utility using Git and Incremental Development
#   References: none
#   Time: 1 hour


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
    for i in list_to_parse:
        if list_to_parse[i] == string_to_find:
            count_num += 1
    return count_num

        
    
    
