class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"""Данные вашего питомца: {self.__name}
                       {self.__animal_type}
                       {self.__age}"""

if __name__ == '__main__':
    animal = Pet("fenya", "cat", 2)
    animal.set_animal_type('dog')

    print(animal.get_animal_type())