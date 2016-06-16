# if and else statements
age = int(input('Input your age: '))
if age < 21:
    print ('Minor')
else:
    print ('Adult')
# if/else works for a string as well
name1 = input('Enter your name (Last name first) : ')
name2 = input('Enter another name (last name first) : ')
if name1 < name2:
    print (name1)
    print (name2)
else:
    print (name2)
    print (name1)

# and/or will work for mutiple questions
pay = int(input('Input your pay: '))
if pay >= 30000:
    years_work = int(input('Input years: '))
    if years_work >= 2:
        print ('Approved')
    else: print ('Go back to work')
else:
    print ('Denied')

# elif is an else if statement
score = int(input('Enter score: '))

if score >= 90:
    print ('Good')
elif score >= 80:
    print ('Ok')
elif score >= 70:
    print ('Eh')
else:
    print ('You suck')








