#Lists
def main():
    in_month, in_day = get_month_and_day()
    print_next_week(in_month, in_day)
    
def print_next_week(in_month, in_day):
    new_month, new_day = calculate_new_day(in_month, in_day)
    print('A week after ' + str(in_month) + \
      '/' + str(in_day) + ' is ' + \
      str(new_month) + '/' + str(new_day))


def calculate_new_day(in_month, in_day):
    month = in_month
    day = in_day
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    print(days_in_month[ 2 : 6]) #this is a slice
    day += 7 # day = day + 7
    if day > days_in_month [month]:
            day -= days_in_month [month]
            month += 1
    return month, day

##   if month == 2 and day > 28:
##        month += 1
##        day -= 28
##    elif ( month == 1 or month == 3 or \
##         month == 5 or month == 7 or \
##         month == 8 or month == 10 or \
##         month == 12 ) and day > 31:
##        month += 1
##        day -= 31
##    elif day > 30:
##        month += 1
##        day -= 30
##
##    if month > 12:
##        month %= 12
##    return month, day
    


def get_month_and_day():
    in_month = int(input('Enter a month(1-12): '))
    in_day = int(input('Enter day(1-31): '))
    return in_month, in_day
main()
