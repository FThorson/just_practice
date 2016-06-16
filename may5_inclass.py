weight1 = float(input('Enter the total weight of the first package: '))
cost1 = float(input('Enter the price of the package: '))
weight2 = float(input('Enter the total weight of the second package: '))
cost2 = float(input('Enter the price of the package: '))

total1 = weight1 // cost1
total2 = weight2 // cost2
print('Cost of package 1 is: ', total1)
print('Cost of package 2 is: ', total2)

if total1 < total2:
    print('Package 1 cost per unit is cheaper at ', total1, ' per unit.')

elif total1 > total2:
    print('Package 2 cost per unit is cheaper at ', total2, ' per unit.')

elif total1 == total2:
    print('Cost per unit of both are the same.')
    
    



