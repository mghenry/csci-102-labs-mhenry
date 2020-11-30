#   Mary Henry
#   ​CSCI 102 – Section G
#   Week 2 - Lab A - Simple Calculator
#   References: 
#   Time: 30 minutes


operand_one = 0.0
operand_two = 0.0

sum = 0.0
difference = 0.0
product = 0.0
quotient = 0.0
remainder = 0.0

print('Input the first operand.')
operand_one = float(input('FIRST>'))

print('Input the second operand.')
operand_two = float(input('SECOND>'))

sum = operand_one + operand_two
difference = operand_one - operand_two
product = operand_one * operand_two
quotient = operand_one / operand_two
remainder = operand_one % operand_two

print('The sum of {} and {} is {:.1f}.'.format(operand_one, operand_two, sum))
print('The difference of {} and {} is {:.1f}.'.format(operand_one, operand_two, difference))
print('The product of {} and {} is {:.1f}.'.format(operand_one, operand_two, product))
print('The quotient of {} and {} is {:.0f}.'.format(operand_one, operand_two, quotient))
print('The remainder of {} and {} is {:.2f}.'.format(operand_one, operand_two, remainder))






