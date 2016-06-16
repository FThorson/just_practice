def my_max(x,y):
    if x < y:
        return y
    else:
        return x
def main():
    x = int(input('Enter a number: '))
    y = int(input('Enter a new number: '))
    z = max (x, y)
    w = my_max(x,y)
    print('The largest of', x, 'and', y, 'is', z)
    print('The largest of', x, 'and', y, 'is', w)
main()










   
        
    

