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
    temp_string_front = string1[:integer]
    temp_string_back = string1[integer:]
    temp_string = temp_string_front + string2 + temp_string_back
    print('OUTPUT', temp_string)


    
    
