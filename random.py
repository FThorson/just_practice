import random
MIN = 9
MAX = 999
QUANTITY = 5
def main():
    print('Here are your five random numbers: ')
    for i in range(QUANTITY):
        ran_num = random.randint(MIN, MAX)
        print(ran_num)
        




main()
