#   Mary Henry
#   ​CSCI 102 – Section G
#   Week 3 - Lab A - Twitter Decoding
#   References: none
#   Time: 20 minutes

phrase = ''

print('Enter the Tweet or Message abbreviation to decode.')
tweet = str(input('TWEET>'))

if tweet == 'IDK':
    phrase = "I don't know"
elif tweet == 'BTW':
    phrase = 'By the way'
elif tweet == 'CU':
    phrase = 'See you'
elif tweet == 'AFAIK':
    phrase = 'As far as I know'
else:
    phrase = "I never heard of that one!"

print('The decoded abbreviation is:')
print('OUTPUT ', tweet, ' = ', phrase)

