# Эта программа расконсервирует объекты Patient:
import class_patient_procedure
import pickle

# Константа для имени файла
FILE_PATIENT = "patient.dot"


def main():
    # Открыть файлы:
    input_file_patient = open(FILE_PATIENT, 'rb')

    # Передаем открытый файл в фунцию
    # для чтения и получаем из нее данные:
    read_file(input_file_patient)


def read_file(file):
    # переменная для обозначения конца файла:
    end_of_file = False

    while not end_of_file:
        try:
            # Расконсервировать следующий объект
            # в созданную переменную для данных
            data = pickle.load(file)
            # Передаем полученные данные в функцию:
            desplay_data(data)
        except EOFError:
            # Установить флаг, чтобы обозначить, что
            # был достигнут конец файла.
            end_of_file = True
        # Закрыть файл.
    file.close()
    # Возвращаем полученные данные в главную функцию
    # return data


# Функция display_data показывает данные
# из объекта переданного в качестве аргумента.
def desplay_data(data):
    print(f'ФИО : {data.get_full_name()}')
    print(f'Адрес, город, область и почтовый индекс: {data.get_phone()}')
    print(f'Имя и телефон контактного лица для экстренной связи: {data.get_contact_phone()}')


if __name__ == '__main__':
    main()
