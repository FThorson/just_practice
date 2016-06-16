# Part 1
year = int(input('Enter a four digit year between 1982 and 2048: '))
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b +4 * c + 6 * d + 5) % 7
day = 22 + d + e
month = 3
if day > 31:
    print('Easter is on: ',month + 1,'/', day - 31)
else:
    print('Easter is on: ', month, '/', day)
# Part 2
print('The following date is the day Easter will be for the years; ')
print('1954, 1981, 2049, and 2076.')
print('So, if you entered any of those four years, ')
print('ignore the first date, and use the second date.')
if year == 1954 or 1981 or 2049 or 2076 and day > 31:
    print('Easter is this day: ', month + 1, '/', day - 38)
else:
    print('Easter is this day: ', month, '/', (day - 7))







