import pickle
import class_patient_procedure

FILE_PATIENT = "patient.dot"
FILE_PROCEDURE = "procedure.dot"


def main():
    # ЗАПИСЬ В ФАЙЛ ДАННЫЕ О ПАЦИЕНТАХ:
    # Variable-question
    out = "да"
    output_file_patient = open(FILE_PATIENT, 'wb')
    while out.lower() == 'да':
        name = input('Ваши имя, отчество и фамилия: ')
        address = input(' Адрес, город, область и почтовый индекс: ')
        phone = input('Телефонный номер: ')
        contact_phone = input('Имя и телефон контактного лица для экстренной связи: ')

        # Create instance of class
        patient = class_patient_procedure.Patient(name, address, phone, contact_phone)

        # picle instance
        pickle.dump(patient, output_file_patient)
        out = input('Вы хотите добавить пациента?(да/нет)?: ')
    output_file_patient.close()
    print(f"Данные записаны в файл {FILE_PATIENT}")

    # Запись в файл о процедурах
    output_file_procedure = open(FILE_PROCEDURE, 'wb')
    count = int(input('Сколько процедур нужно пройти пациенту?: '))
    # total_cost_procedures = 0
    for procedure in range(count):
        proc_name = input('Название процедуры: ')
        proc_date = input('Дата процедуры: ')
        doc_name = input('Имя врача, который выполнял процедуру: ')
        cost_proc = float(input('Стоимость процедуры: '))

        # create instance of class Procedure:
        procedure = class_patient_procedure.Procedure(proc_name, proc_date, doc_name, cost_proc)
        pickle.dump(procedure, output_file_procedure)
    output_file_procedure.close()
    print(f"Данные записаны в файл {FILE_PROCEDURE}")



if __name__ == '__main__':
    main()
