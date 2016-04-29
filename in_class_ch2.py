# A bu 6 chi.
# A li was 300 bu.


#this program will convert
# a number of chi into
# appropiate numbers of
# li, bu, and chi

BU_PER_LI = 300
CHI_PER_BU = 6

print ('We will convert chi to')
print ('li, bu, and chi, where')
print ('a li is 300 bu')
print ('a bu is 6 chi')
CHI = int(input('How many chi? '))
# make a temporary count of chi
# to be reduced to li, bu, and chi
chi_change = CHI

# count li
LI = chi_change // \
     (CHI_PER_BU * BU_PER_LI)
chi_change = chi_change % \
             (CHI_PER_BU * BU_PER_LI)

# count bu
BU = chi_change // CHI_PER_BU
chi_change = chi_change % CHI_PER_BU

# display results
print (CHI, 'chi is: ')
print (LI, 'li, ', BU, 'bu,', \
       chi_change, 'chi')

print ('We will compute the average of three numbers.')
x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
z = int(input('Enter a third number: '))
value = (x + y + z) / 3
print ('The average is: ', value)

import math
num_dogs = int(input('Enter number of hot dogs: '))
num_buns = int(input('Enter number of buns: '))
total = num_dogs + num_buns





