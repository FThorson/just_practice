#Basic Triangle
for line in range(1,6):
    for i in range(1,line + 1):
        print(i, end = ' ')
    print()
    
#Upside Down Triangle
print()
for line in range(5,0, -1):
    for i in range(1,line + 1):
        print(i, end = ' ')
    print()

#Right-Justified Triangle
for line in range(1,6):
    for i in range(-2 * line + 10):
        print(end = ' ')
    for i in range(line, 0, -1):
        print(i, end = ' ')
    print()

#Right-Justified Triangle Part 2
print()
for line in range(5,0, -1):
    for i in range(-2 * line + 10):
        print(end = ' ')
    for i in range(1, line +1):
        print(i, end = ' ')
    print()

#Next
sum = 0
for i in range(1, 98, 2):
    sum += i / (i + 2)
print('Fraction sum = ' ,sum)

#Next
count = 0
for first in range(1, 8):
    for second in range(first + 1, 8):
        print(first, second)
        count += 1
print('Count = ', count)

#Next
n = int(input('Input a number: '))
count = 0
for first in range(1, n + 1):
    for second in range(first + 1, n + 1):
        print(first, second)
        count += 1
print('Count = ', count)

#Next
print()
num = 1
for line in range(1, 10):
    product = num * 8 + line
    print(num, '* 8 +', line, '=', product)
    num = num * 10 + line + 1

#Next
print()
num = 1
for line in range(1, 10):
    product = num * 9 + line + 1
    print(num, '* 9 +', line + 1, '=', product)
    num = num * 10 + line + 1

#Next
print()
num = 1
for line in range(1, 10):
    print (num * num)
    num = 10 * num +1





