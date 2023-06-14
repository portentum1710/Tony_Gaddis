# Эта программа расконсервирует объекты Patient and Procedure:
import class_patient_procedure
import pickle

# Константы для имени файла
FILE_PATIENT = "patient.dot"
FILE_PROCEDURE = "procedure.dot"


def main():
    # Открыть файлы:
    input_file_patient = open(FILE_PATIENT, 'rb')
    input_file_procedure = open(FILE_PROCEDURE, 'rb')

    # Передаем открытые файлы в фунцию
    # для чтения и получаем из нее данные:
    read_file(input_file_patient)
    read_file(input_file_procedure)


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
    print(data)


if __name__ == '__main__':
    main()
