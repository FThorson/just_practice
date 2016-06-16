continue_counting = 'y'
while continue_counting == 'y':
    day1 = int(input('Number of bugs, day 1: '))
    day2 = int(input('Number of bugs, day 2: '))
    day3 = int(input('Number of bugs, day 3: '))
    day4 = int(input('Number of bugs, day 4: '))
    day5 = int(input('Number of bugs, day 5: '))
    total = day1 + day2 + day3 + day4 + day5
    print('Total amount of bugs is: ', total)
    continue_counting = input('Would you like to continue counting? (Enter y for yes): ')

