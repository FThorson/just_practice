keep_counting = 'y'

while keep_counting == 'y':
    cents_quarters = 25
    cents_dimes = 10
    cents_nickels = 5
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))

    total_cents = cents_quarters * quarters \
      + cents_dimes * dimes \
      + cents_nickels  * nickels \
      + pennies
    print( quarters, 'quarters',
       dimes, 'dimes',
       nickels, 'nickels',
       pennies, 'pennies',
       'is', total_cents, 'cents.')
    keep_counting = input('Would you like to continue with more coins?(Enter y for yes): ')

