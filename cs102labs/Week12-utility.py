#   Maggie Henry
#   CSCI 102 – Section G
#   Week 12 - Utility using Git and Incremental Development
#   References: none
#   Time: 1 hour


def load_file("some_file_name.txt"):
    file_to_read = open("some_file_name.txt")
    file_list = file_to_read.readlines()
    file_to_read.close()
    return file_list


file_test = input("file:")
lines = load_file(file_test)
print('OUTPUT', lines)
