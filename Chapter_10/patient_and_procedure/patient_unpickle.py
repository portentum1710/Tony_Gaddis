import class_patient_procedure
import pickle

FILENAME = "procedure.dot"


def main():
    input_file = open(FILENAME, 'rb')
    end_of_file = False

    while not end_of_file:
        try:
            pat_data = pickle.load(input_file)
            desplay_data(pat_data)
        except EOFError:
            end_of_file = True

    input_file.close()


def desplay_data(pat_data):
    print(type(pat_data))
    print(f'ФИО: {pat_data.get_full_name()}')
    print(f'Адрес, город, область и почтовый индекс: {pat_data.get_full_address()}')
    print(f'Телефонный номер: {pat_data.get_phone()}')
    print(f'Имя и телефон контактного лица для экстренной связи: {pat_data.get_contact_phone()}')
    print('----------------------------------------------------')
    # print(f'Название процедуры: {pat_data.}')
    # print(f'Дата процедуры: {class_patient_procedure.Procedure.get_procedure_date(self=)}')
    # print(f'Имя врача, который выполнял процедуру: {class_patient_procedure.Procedure.get_doctor_name(self=)}')
    # print(f'Стоимость процедуры: {class_patient_procedure.Procedure.get_cost_procedure(self=)}')


if __name__ == '__main__':
    main()