# Эта программа управляет контактами.
import contact
import pickle

# Глобальные константы для пунктов меню.
LOOK_UP = 1  # НАЙТИ
ADD = 2  # ДОБАВИТЬ
CHANGE = 3  # ИЗМЕНИТЬ
DELETE = 4  # УДАЛИТЬ
QUIT = 5  # ВЫЙТ

# Глобальная константа для имени файла.
FILENAME = 'contacts.dat'


# Главная функция.
def main():
    mycontantcs = load_contacts()
    # Инициализировать переменную для выбора пользователя.
    choice = 0

    # Обрабатывать варианты выбора пунктов меню до тех пор,
    # пока пользователь не пожелает выйти из программы.
    while choice != QUIT:
        # Получить выбранный пользователем пункт меню.
        choice = get_menu_choice()
        # Обработать выбранный вариант действий.
        if choice == LOOK_UP:
            look_up(mycontantcs)
        elif choice == ADD:
            add(mycontantcs)
        elif choice == CHANGE:
            change(mycontantcs)
        elif choice == DELETE:
            delete(mycontantcs)
    # Сохранить словарь mycontacts в файле.
    save_contacts(mycontantcs)


def load_contacts():
    try:
        # Открыть файл contacts.dat
        input_file = open(FILENAME, 'rb')

        # Расконсервировать словарь.
        contact_dct = pickle.load(input_file)

        # Закрыть файл phone_inventory.dat.
        input_file.close()
    except IOError:
        # Не получилось открыть файл, поэтому
        # создать пустой словарь.
        contact_dct = {}

    # Вернуть словарь.
    return contact_dct


# Функция get_menu_choice выводит меню и получает
# проверенный на допустимость выбранный пользователем пункт.
def get_menu_choice():
    print()
    print('Меню')
    print('----------------------------------------')
    print('1. Найти контактное лицо')
    print('2. Добавить новое контактное лицо')
    print('3. Изменить существующее контактное лицо')
    print('4. Удалить контактное лицо')
    print('5. Выйти из программы')
    print()

    # Получить выбранный пользователем пункт меню.
    choice = int(input('Введите выбранный пункт:'))

    # Проверить выбранный пункт на допустимость.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт:'))

    # Вернуть выбранный пользователем пункт.
    return choice


# Функция look_up отыскивает элемент
# в заданном словаре.
def look_up(mycontacts):
    # Получить искомое имя.
    name = input('Введите имя:')

    # Отыскать его в словаре.
    print(mycontacts.get(name, 'Это имя не найдено'))

# Функция add добавляет новую запись
# в указанный словарь.
def add(mycontacts):
    # Получить контактную информацию.
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input("Электронный адрес: ")

    # Создать именованную запись с объектом Contact.
    entry = contact.Contact(name, phone, email)

    # Если имя в словаре не существует, то
    # добавить его в качестве ключа со связанным с ним
    # значением в виде объекта.
    if name not in mycontacts:
        mycontacts[name] = entry
        print('Запись добавлена.')
    else:
        print('Это имя уже существует.')

# Функция change изменяет существующую
# запись в указанном словаре.
def change(mycontacts):
    # Получить искомое имя.
    name = input('Введите имя: ')

    if name in mycontacts:
        # Получить новый телефонный номер.
        phone = input('Введите новый телефонный номер: ')

        # Получить новый электронный адрес.
        email = input('Введите новый электронный адрес: ')

        # Создать именованную запись с объектом Contact.
        entry = contact.Contact(name, phone, email)

        # Обновить запись
        mycontacts[name] = entry
        print('Информация обновлена.')
    else:
        print("Это имя не найдено.")

# Функция delete удаляет запись
# из указанного словаря.
def delete(mycontacts):
    # Получить искомое имя.
    name = input('Введите имя: ')

    # Если имя найдено, то удалить запись.
    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена.')
    else:
        print("Это имя не найдено.")
