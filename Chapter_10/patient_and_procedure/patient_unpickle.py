import class_patient_procedure
import pickle

FILENAME = "procedure.dot"


def main():
    input_file = open(FILENAME, 'rb')
    end_of_file = False

    while not end_of_file:
        try:
            patient = pickle.load(input_file)
            desplay_data(patient)
        except EOFError:
            end_of_file = True

    input_file.close()


def desplay_data(patient):
    print(type(patient))
    print(f'ФИО: {patient.get_full_name()}')
    print(f'Адрес, город, область и почтовый индекс: {patient.get_full_address()}')
    print(f'Телефонный номер: {patient.get_phone()}')
    print(f'Имя и телефон контактного лица для экстренной связи: {patient.get_contact_phone()}')
    print('----------------------------------------------------')
    print(f'Название процедуры: {class_patient_procedure.Procedure.get_name_procedure()}')
    print(f'Дата процедуры: {class_patient_procedure.Procedure.get_procedure_date()}')
    print(f'Имя врача, который выполнял процедуру: {class_patient_procedure.Procedure.get_doctor_name()}')
    print(f'Стоимость процедуры: {class_patient_procedure.Procedure.get_cost_procedure()}')


if __name__ == '__main__':
    main()