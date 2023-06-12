class RetailItem:
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def set_name(self, name):
        self.__name = name

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    