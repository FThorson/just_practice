# Number 1
for i in range(1,7):
    print(2*i, ' ', end='')
print('End number 1')


# Number 4              
print("Let's do a count down")

for i in range(1,11):
    print( 11 - i, ', ', sep='')
print('Blast off!!!')
print('Next') # number 5
sum = 0.0
for i in range(1,31):
    sum += i / 30
print('1/30 + 2/30 + ... + 30/30 =', sum)

print('Next') # Number 6

SQUARES = 64

num_on_square = 1
total = 0

for sq in range(SQUARES):
    print('On square', (sq+1),
          'grains =', format(num_on_square, ','))
    total += num_on_square
    num_on_square *= 2

print( 'Total =', format(total, ','))

print('Next') # Number 7

for row in range(6):
    for col in range(5):
        print((row,col), end = ' ')
    print()

print('Next') # Number 9

print()
print('     ', end = '')
for i in range(1,13):
    print(format(i, '4d'), end = '')
print()

print('     ', end = '')
for i in range(1,13):
    print('_____', end = '')
print('___')

for x in range(1,13):
    print(format(x, '2d'), '|', end = '')
    for y in range(1,13):
        print(format(x * y, '4d'), end = '')
    print()







