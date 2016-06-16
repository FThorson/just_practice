distance_traveled = 'y'
while distance_traveled == 'y':
    speed = int(input('Enter the speed driven: '))
    hours = int(input('Enter the hours driven: '))
    distance = speed * hours
    print('The distance traveled is: ', distance, ' miles.')
    distance_traveled = input('Another trip? (enter "y" for yes): ')
    
