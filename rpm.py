# russian peasant multiplication
def main():
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))

    t1 = a
    t2 = b

    product = 0;

    while t2 > 0:
        if t2 % 2 == 1:
            product += t1
        t1 *= 2
        t2 //= 2

    print(a, 'times', b, '=', product)

main()
    
