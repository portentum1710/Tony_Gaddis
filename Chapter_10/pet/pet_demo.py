import pet

def main():
    name = input('Введите имя питомца: ')
    animal_type = input('Введите тип питомца(кошка, собака и т.д): ')
    age = input('Введите возраст питомца: ')

    new_pet = pet.Pet(name, animal_type, age)
    print(new_pet)

if __name__ == '__main__':
    main()