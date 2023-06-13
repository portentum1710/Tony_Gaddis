import pickle
import class_patient_procedure

FILENAME = "procedure.dot"


def main():
    # Variable-question
    out = "нет"
    output_file = open(FILENAME, 'wb')

    while out.lower() == 'нет':
        name = input('Ваши имя, отчество и фамилия: ')
        address = input(' Адрес, город, область и почтовый индекс: ')
        phone = input('Телефонный номер: ')
        contact_phone = input('Имя и телефон контактного лица для экстренной связи: ')

        # Create instance of class
        patient = class_patient_procedure.Patient(name, address, phone, contact_phone)
        # picle instance
        pickle.dump(patient, output_file)
        count = int(input('Сколько процедур нужно пройти пациенту?: '))
        # total_cost_procedures = 0
        for procedure in range(count):
            proc_name = input('Название процедуры: ')
            proc_date = input('Дата процедуры: ')
            doc_name = input('Имя врача, который выполнял процедуру: ')
            cost_proc = float(input('Стоимость процедуры: '))
            # total_cost_procedures += cost_proc
            # Create instance of class
            procedure = class_patient_procedure.Procedure(proc_name, proc_date, doc_name, cost_proc)
            pickle.dump(procedure, output_file)
        out = input('Вы хотите выйти из программы(да/нет)?: ')

    output_file.close()
    print(f"Данные записаны в файл {FILENAME}")

if __name__ == '__main__':
    main()