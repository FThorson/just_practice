def main():
    year = get_year()
    print(year)
    zodiac_animal(year)

def get_year():
  new_year = int(input('Enter a year: '))
  return new_year

def zodiac_animal(year):
    animal_year = year % 12
    animals = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', \
               'Dragon', 'Snake', 'Horse', 'Sheep']
    print('Your zodiac animal is: ', animals[animal_year])

main()
