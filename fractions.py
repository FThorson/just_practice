n = int(input('Enter a number: '))
sum = 1.0
for n in range(1, n + 1):
    sum += 1 / n
    print('1/1 + 1/2 + 1/3 + ... + 1/n =', sum)
for n in range(n, n +1):
    sum += n / 1
    print('n/1 + n/2 + ... + n/n + ... + 2/n + 1/n =', sum)


