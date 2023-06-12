# This programma will de-conserve object Pet
import pickle
import pet

FILENAME = "petshop.dat"


def main():
    # Variable for indicate the end of file
    end_of_file = False

    # Open the file:
    input_file = open(FILENAME, 'rb')
    # Read to the end of file:
    while not end_of_file:
        try:
            # de-conserve object:
            animal = pickle.load(input_file)
            # To show date about pet
            display_data(animal)
            print('---------------------------')
        except EOFError:
            # Set a flag to indicate that
            # the end of the file has been reached
            end_of_file = True
    input_file.close()


# Function display_data shows data from PetObject pessed as an argument
def display_data(animal):
    # print(animal)
    print(f'Name of your pet: {animal.get_name()}')
    print(f'Type of your animal: {animal.get_animal_type()}')
    print(f'That how old your pet is: {animal.get_age()}')


if __name__ == '__main__':
    main()
