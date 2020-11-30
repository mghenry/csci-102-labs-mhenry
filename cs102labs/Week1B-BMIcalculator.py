#   Maggie (Mary) Henry
#  ​ CSCI 102 – Section G
#   Week 1 - Part B
#   References: no one
#   Time: 10 minutes
#BMI Calculator

import math

print('Input your weight in pounds')
weight = int(input('WEIGHT> '))

print('Input your height in inches')
height = int(input('HEIGHT> '))

weight *= 0.454
height *= 0.0254

bmi = weight/math.pow(height, 2)
bmi = round(bmi, 1)

print('Your body-mass index is:')
print('OUTPUT', bmi)
