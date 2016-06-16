import math

def main():
    side_length = get_side_length()
    
    report(side_length)
    
    
    
       
def report( side_length ):
    for num_sides in range(3,10):
        area = polygon_area (num_sides, side_length)
        print('Side Length          Number of Sides      Area')
        print(side_length, '                    ',num_sides,'                 ',format(area, '2.2f'))
        
    
    
    

def polygon_area( num_sides, side_length ):
    area = (num_sides * side_length * side_length) \
           / (4 * math.tan(math.pi / num_sides))
    return area

    
def get_side_length():
    side_length = int(input('Enter the side length: '))
    return side_length
    


main()
