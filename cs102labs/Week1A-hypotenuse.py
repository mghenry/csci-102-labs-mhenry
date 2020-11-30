#   Maggie (Mary) Henry
#  ​ CSCI 102 – Section G
#   Week 1 - Part A
#   References: no one
#   Time: 10 minutes
#calculating the hypoteneuse of a triangle

import math

print('Input an integer value for the first leg of a triangle:')
print('A>')
a = int(input())

print('Input another integer value for the second leg of a triangle:')
print('B>')
b = int(input())

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print('The value of the hypoteneuse of your triangle is:')
print('OUTPUT', c)
