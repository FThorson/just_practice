import random
MIN = 0
MAX = 9
QUANTITY = 7
def main():
    print('Here are the seven lottery numbers: ')
    for i in range(QUANTITY):
        ran_num = random.randint(MIN, MAX)
        print(ran_num)
main()
