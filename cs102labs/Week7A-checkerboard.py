#   Maggie Henry
#   CSCI 102 – Section G
#   Week 7 - Lab A - Checkerboard
#   References: none
#   Time: 45 minutes

print('Input an integer value for the dimensions of the checkerboard:')
n = int(input())
print('Input the first checker:')
elem1 = str(input())
print('Input the second checker:')
elem2 = str(input())

rows, cols = (n, n)
check = []

row1 = []
for i in range(n):
    if (i - 1) % 2 == 0:
        row1.append(elem1)
    else:
        row1.append(elem2)

row2 = []
for i in range(n):
    if (i - 1) % 2 == 0:
        row2.append(elem2)
    else:
        row2.append(elem1)


for i in range(n):
    if (i - 1) % 2 == 0:
        check.append(row1)
    else:
        check.append(row2)
        
for i in range(n):
    print('OUTPUT ', check[i])
          
print('OUTPUT ', check)


