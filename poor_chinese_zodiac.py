# Poor Chinese Zodiac Calculator

year = int(input('Enter a year: '))

animal_year = year % 12

if animal_year == 0:
    print(year, 'is the year of the monkey')
elif animal_year == 1:
    print(year, 'is the year of the rooster')
elif animal_year == 2:
    print(year, 'is the year of the dog')
elif animal_year == 3:
    print(year, 'is the year of the pig')
elif animal_year == 4:
    print(year, 'is the year of the rat')
elif animal_year == 5:
    print(year, 'is the year of the ox')
elif animal_year == 6:
    print(year, 'is the year of the tiger')
elif animal_year == 7:
    print(year, 'is the year of the rabbit')
elif animal_year == 8:
    print(year, 'is the year of the dragon')
elif animal_year == 9:
    print(year, 'is the year of the snake')
elif animal_year == 10:
    print(year, 'is the year of the horse')
else:
    print(year, 'is the year of the sheep')

