class Patient:
    def __init__(self, full_name, full_address, phone, contact_phone):
        self.__full_name = full_name
        self.__full_address = full_address
        self.__phone = phone
        self.__contac_phone = contact_phone

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_full_address(self, full_address):
        self.__full_address = full_address

    def set_phone(self, phone):
        self.__phone = phone

    def set_contact_phone(self, contact_phone):
        self.__contac_phone = contact_phone

    def get_full_name(self):
        return self.__full_name

    def get_full_address(self):
        return self.__full_address

    def get_phone(self):
        return self.__phone

    def get_contact_phone(self):
        return self.__contac_phone

    def __str__(self):
        return f"""ФИО:                                                 {self.__full_name}
                   Адрес, город, область и почтовый индекс:             {self.__full_address}
                   Телефонный номер:                                    {self.__phone}
                   Имя и телефон контактного лица для экстренной связи: {self.__contac_phone}
                """


class Procedure:
    def __init__(self, proc_name, proc_date, doc_name, cost_proc):
        self.__name_of_procedure = proc_name
        self.__procedure_date = proc_date
        self.__doctor_name = doc_name
        self.__cost_procedure = cost_proc

    def set_name_procedure(self, proc_name):
        self.__name_of_procedure = proc_name

    def set_procedure_date(self, proc_date):
        self.__procedure_date = proc_date

    def set_doctor_name(self, doc_name):
        self.__doctor_name = doc_name

    def set_cost_procedure(self, cost_proc):
        self.__cost_procedure = cost_proc

    def get_name_procedure(self):
        return self.__name_of_procedure

    def get_procedure_date(self):
        return self.__procedure_date

    def get_doctor_name(self):
        return self.__doctor_name

    def get_cost_procedure(self):
        return self.__cost_procedure

    def __str__(self):
        return f""""  Название процедуры:                    {self.__name_of_procedure}
                      Дата процедуры:                        {self.__procedure_date}  
                      Имя врача, который выполнял процедуру: {self.__doctor_name}
                      Cтоимость процедуры:                   {self.__cost_procedure}
                """
