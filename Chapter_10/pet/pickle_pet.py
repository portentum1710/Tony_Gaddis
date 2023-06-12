import pet
import pickle

FILENAME = "petshop.dat"


def main():
    # Constant for file name.
    # initialize a varible for control loop
    again = 'y'

    # Open the file.
    output_file = open(FILENAME, 'wb')

# Get data from user:
    while again.lower() == 'y':
        name = input('Введите имя питомца: ')
        animal_type = input('Введите тип питомца(кошка, собака и т.д): ')
        age = input('Введите возраст питомца: ')

        # Create object Pet
        new_pet = pet.Pet(name, animal_type, age)

        # Preserve the object and write it to a file:
        pickle.dump(new_pet, output_file)

        # Get anothe data item?
        again = input("Введите еще одного питомца? (y/n):")

    # Close the file
    output_file.close()
    print(f"Данные записаны в {FILENAME}")


if __name__ == '__main__':
    main()
