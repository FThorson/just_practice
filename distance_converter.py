#convert miles to inches
#convert feet to inches

print('We will convert miles to feet and feet to inches.')
miles = int(input('Enter the number of miles: '))
feet = int(input('Enter the number of feet: '))
inches = int(input('Enter the number of inches: '))
total_feet = int(feet + (miles * 5280))
total_inches = int(inches + (feet * 12))
print ('Number of feet is: ', total_feet)
print ('Total number of inches is: ', total_inches)

