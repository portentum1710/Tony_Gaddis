# Константа для ставки налога с продаж.
TAX_RATE = 0.05


# Класс ServiceQuote.
class ServiceQuote:
    def __init__(self, pcharge, lcharges):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharges

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self, lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        return self.__parts_charges * TAX_RATE

    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges + \
            (self.__parts_charges * TAX_RATE)
