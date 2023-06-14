# Эта программа консервирует объекты Patient and Procedure
import pickle
import class_patient_procedure

# Константы для имен файлов.
FILE_PATIENT = "patient.dot"
FILE_PROCEDURE = "procedure.dot"


def main():
    # Инициализировать переменную для управления циклом:
    out = "да"

    # Открыть файл для записи данных о пациенте(тах):
    output_file_patient = open(FILE_PATIENT, 'wb')

    # Получить данные от пользователя.
    while out.lower() == 'да':
        name = input('Ваши имя, отчество и фамилия: ')
        address = input(' Адрес, город, область и почтовый индекс: ')
        phone = input('Телефонный номер: ')
        contact_phone = input('Имя и телефон контактного лица для экстренной связи: ')

        # Создать объект Patient
        patient = class_patient_procedure.Patient(name, address, phone, contact_phone)

        # Законсервировать объект и записать его в файл.
        pickle.dump(patient, output_file_patient)

        # Получить еще один элемент данных?
        out = input('Вы хотите добавить пациента?(да/нет)?: ')

        # Закрыть файл.
    output_file_patient.close()
    print(f"Данные записаны в файл {FILE_PATIENT}")

    # Открыть файл для записи данных о процедурах
    output_file_procedure = open(FILE_PROCEDURE, 'wb')

    # Инициализировать переменную для управления циклом:
    count = int(input('Сколько процедур нужно пройти пациенту?: '))

    # Получить данные от пользователя.
    for procedure in range(count):
        proc_name = input('Название процедуры: ')
        proc_date = input('Дата процедуры: ')
        doc_name = input('Имя врача, который выполнял процедуру: ')
        cost_proc = float(input('Стоимость процедуры: '))

        # Создать объект Procedure:
        procedure = class_patient_procedure.Procedure(proc_name, proc_date, doc_name, cost_proc)

        # Законсервировать объект и записать его в файл.
        pickle.dump(procedure, output_file_procedure)

    # Закрыть файл.
    output_file_procedure.close()
    print(f"Данные записаны в файл {FILE_PROCEDURE}")



if __name__ == '__main__':
    main()
