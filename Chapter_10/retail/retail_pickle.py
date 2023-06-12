import pickle
import retail_item

FILENAME = "retail.dat"


def main():
    # Flag that stop loop
    again = "y"
    output_file = open(FILENAME, 'wb')

    while again.lower() == "y":
        name = input('Ввидите наименование товара: ')
        quantity = int(input('Ввидите кол-во товара: '))
        price = float(input('Ввидите цену товара: '))

        # Создаем объект, на основании введенных данных:
        new_item = retail_item.RetailItem(name, quantity, price)

        # Консервируем объект и записываем файл:
        pickle.dump(new_item, output_file)

        # Получить еще один элемент данных?
        again = input("Введете еще одну еденицу товара?(y/n): ")

    # Закрыть файл
    output_file.close()
    print(f'Данные записаны в файл {FILENAME}')

if __name__ == '__main__':
    main()

