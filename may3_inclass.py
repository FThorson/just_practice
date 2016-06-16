month = int(input('Enter a month (1-12): '))
day = int(input('Enter a day (1-31): '))

new_month = month + 1
new_day = day + 7

if month == 2 and day > 28:
    new_month += 1
    new_day -= 28
    
elif (month == 1 or month == 3 or month == 5 or month == 7 or
    month == 8 or month == 10 or month == 12)
      and new_day > 31:
    new_month += 1
    new_day -= 31
    
elif new_day > 30 and month != 12:
    new_month + 1
    new_day -= 30

elif month == 12 and new_day > 31:
    new_day = 1
    new_month -= 31
    
print ('a week after ', month, '/', day,
       ' is ', new_month, '/', new_day, sep = '')


    
