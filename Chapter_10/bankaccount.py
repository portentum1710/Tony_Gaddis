# Класс Bankaccount иммитирует банковский счет
# Метод __init__ принимает аргумент с остатком на счете
# Он присваевается атрибуту __balance.

class Bankaccount:
    def __init__(self, bal):
        self.__balance = bal

# Метод deposit вносит на счет вклад:
    def deposit(self, amount):
        self.__balance += amount

# Метод withdraw снимаем со счета сумму:
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Ошибка: недостаточно средств!")

# Метод get_balance возвращаем остаток средств на счете
    def get_balance(self):
        return self.__balance
