
# Эта программа расконсервирует объекты CellPhone
import pickle
import cellphone

FILENAME = 'cellphones.dat'


def main():
    end_of_file = False  # Переменная для обозначения конца файла

    # Открыть файл
    input_file = open(FILENAME, 'rb')

    # Прочитать до конца файла.
    while not end_of_file:
        try:
            # Расконсервиравать следующий объект.
            phone = pickle.load(input_file)
            # Показать данные о сотовом телефоне.
            display_data(phone)
        except EOFError:
            # Установить флаг, чтобы обозначить, что
            # был достигнут конец файла.
            end_of_file = True
    # Закрыть файл.
    input_file.close()

# Функция display_data показывает данные
# из объекта CellPhone, переданного в качестве аргумента.


def display_data(phone):
    print(f'Производитель: {phone.get_manufact}')
    print(f'Номер модели: {phone.get_model}')
    print(f'Розничная цена: {phone.get_retail_price():,.2f}')


if __name__ == '__main__':
    main()
