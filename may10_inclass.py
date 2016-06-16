speed = int(input('Enter the speed: '))
hour = 1
while hour <= 5:
    distance = hour * speed
    print(hour, distance)
    hour += 1

print('*****')

for hour in range(1,6):
    distance = hour * speed
    print(hour, distance)
    hour += 1

print('*****')

for hour in range(5,0,-1):
    distance = hour * speed
    print(hour, distance)
    hour += 1

print('*****')

for hour in range(1,10,2):
    distance = hour * speed
    print(hour, distance)
    hour += 1

keep_going = 'y'
while keep_going == 'y':
    sales = float(input('Amount of sales: '))
    comm_rate = float(input('Commission rate: '))
    commission = sales * comm_rate
    print('Commission is: ', commission)
    keep_going = input('Another commission? (Enter y for yes): ')
    
