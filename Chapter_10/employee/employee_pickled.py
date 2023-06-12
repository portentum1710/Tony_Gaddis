import employee_class
import pickle

FILENAME = 'employee.dat'

output_file = open(FILENAME, 'wb')


def main():
    # initialized a variable for control loop
    again = "y"
    while again.lower() == "y":
        name = input("Введите имя сотрудника: ")
        emp_id = input("Введите Идентификационный номер сотрудника: ")
        division = input("Введите Отдел для сотрудника: ")
        emp_position = input("Введите должность сотрудника: ")
        print()

        new_employee = employee_class.Employee(name, emp_id, division, emp_position)
        pickle.dump(new_employee, output_file)
        # Получить еще один элемент данных?
        again = input("Введете ещё одного сотрудника? (y/n): ")

    output_file.close()
    print(f"Данные записаны в {FILENAME}")

if __name__ == '__main__':
    main()