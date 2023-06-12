class Employee:
    def __init__(self, name, emp_id, division, emp_position):
        self.__name = name
        self.__emp_id = emp_id
        self.__division = division
        self.__emp_position = emp_position

    def set_name(self, name):
        self.__name = name

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_division(self, division):
        self.__division = division

    def set_emp_position(self, emp_posiotion):
        self.__emp_position = emp_posiotion

    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id

    def get_division(self):
        return self.__division

    def get_emp_position(self):
        return self.__emp_position
