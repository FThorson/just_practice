lets_go = 'y'
while lets_go == 'y' :
    num_one = int(input('Enter a number: '))
    num_two = int(input('Enter a number: '))
    print(num_one, '+', num_two, '=', num_one + num_two)
    lets_go = input('Ready to go? (y,n): ')
#Next
for i in range(0, 1000, 10):
    print(i, end = ', ')
print(1000)
#Next
x = 0
while x <= 0 or x > 100:
    x = int(input('Enter a number 1 to 100: '))
    if x <= 0:
        print('Invalid, try again.')
    elif x > 100:
        print('Too high, try again.')




