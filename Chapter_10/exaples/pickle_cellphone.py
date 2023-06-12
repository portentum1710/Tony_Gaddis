# Эта программа консервирует объекты CellPhone.
import pickle
import cellphone

# Константа для имени файла
FILENAME = 'cellphones.dat'


def main():
    # Инициализировать переменную для управления циклом.
    again = 'y'

    # Открыть файл.
    output_file = open(FILENAME, 'wb')

    # Получить данные от пользователя.
    while again.lower() == 'y':
        # Получить данные о сотовом телефоне.
        man = input('Введите производителя:')
        mod = input('Введите номер модели:')
        retail = float(input('Введите розничную цену:'))

        # Создать объект CellPhone.
        phone = cellphone.CellPhone(man, mod, retail)

        # Законсервировать объект и записать его в файл.
        pickle.dump(phone, output_file)
        # Получить еще один элемент данных?
        again = input('Введите еще один элемент данных? (y/n):')

    # Закрыть файл.
    output_file.close()
    print(f'Данные записаны в {FILENAME}')


# Вызвать главную функцию.
if __name__ == '__main__':
    main()

