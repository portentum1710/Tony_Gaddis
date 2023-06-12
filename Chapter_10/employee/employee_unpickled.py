import employee_class
import pickle

FILENAME = "employee.dat"


def main():
    end_of_file = False  # Переменная для обозначения конца файла

    # Открыть файл
    input_file = open(FILENAME, "rb")

    # Прочитать до конца файла.
    while not end_of_file:
        try:
            # Расконсервиравать следующий объект
            employees = pickle.load(input_file)
            # Показать данные о сотрудниках:
            desplay_emps(employees)
        except EOFError:
            # Установить флаг, чтобы обозначить, что
            # был достигнут конец файла
            end_of_file = True
    # Закрыть файл.
    input_file.close()


def desplay_emps(employees):
    print(f"Имя сотрудника: {employees.get_name()}")
    print(f"Идентификационный номер сотрудника: {employees.get_emp_id()}")
    print(f"Отдел сотрудника: {employees.get_division()}")
    print(f"Должность сотрудника: {employees.get_emp_position()}")
    print()
    #print(employees)


if __name__ == '__main__':
    main()