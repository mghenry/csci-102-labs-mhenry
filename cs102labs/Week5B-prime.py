#   Maggie Henry
#   ​CSCI 101 – Section G
#   Week 5 - Lab B - Prime Factors
#   References: internet
#   Time: 30 minutes


user_in  = 'yes'
i = int()

while user_in == 'y' or 'Y' or 'yes' or 'YES' or 'yES' or 'Yes' or 'yEs' or 'YEs' or 'YeS':

    print('Enter a positive integer to generate its prime factors:')
    number = int(input('INPUT>'))
    orig = number

    num_list = []
    d = 2


    while (d*d <= number):
        if (number % d != 0):
            d += 1
        else:
            number /= d
            num_list.append(d)   
        
    if number > 1:
        num_list.append(number)

    print('The prime factors of the integer', orig, 'are:')
    print('OUTPUT', *num_list, sep="*")

    print('Do you want to get the prime factors for another input?')
    user_in  = input()


print('Goodbye!')

    





