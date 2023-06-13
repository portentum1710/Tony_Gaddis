import class_patient_procedure
import pickle

FILE_PATIENT = "patient.dot"
FILE_PROCEDURE = "procedure.dot"


def main():
    input_file_patient = open(FILE_PATIENT, 'rb')
    input_file_procedure = open(FILE_PROCEDURE, 'rb')

    end_of_file = False
    # Расконсервируем файл поциента
    while not end_of_file:
        try:
            data = pickle.load(input_file_patient)
            desplay_data(data)
        except EOFError:
            end_of_file = True
    input_file_patient.close()

    end_of_file = False
    # Расконсервируем файл с процедурами:
    while not end_of_file:
        try:
            data = pickle.load(input_file_procedure)
            desplay_data(data)
        except EOFError:
            end_of_file = True
    input_file_procedure.close()


def desplay_data(data):
    print(data)


if __name__ == '__main__':
    main()
