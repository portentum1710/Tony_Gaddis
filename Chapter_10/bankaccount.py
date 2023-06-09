# Класс Bankaccount иммитирует банковский счет
# Метод __init__ принимает аргумент с остатком на счете
# Он присваевается атрибуту __balance.

class Bankaccount:
    def __init__(self, bal):
        self.__balance = bal
