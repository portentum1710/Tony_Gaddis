# Эта программа расконсервирует объекты Procedure:
import class_patient_procedure
import pickle

# Константа для имени файла:
FILE_PROCEDURE = "procedure.dot"



def main():
    # Открыть файл:
    input_file_procedure = open(FILE_PROCEDURE, 'rb')

    # Передаем открытый файл в фунцию
    # для чтения и получаем из нее данные
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


# Функция display_data показывает данные
# из объекта переданного в качестве аргумента.
def desplay_data(data):
    print(f'Название процедуры: {data.get_name_procedure()}')
    print(f'Дата процедуры: {data.get_procedure_date()}')
    print(f'Имя врача, который выполнял процедуру: {data.get_doctor_name()}')
    print(f'Cтоимость процедуры: {data.get_cost_procedure():,.2f}')
    print("----------------------------------------")


if __name__ == '__main__':
    main()
