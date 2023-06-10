import bankaccount


def main():
    # Получить начальный остаток:
    start_balance = float(input("Введите свой начальный остаток"))
    # Создать объект BankAccount
    savings = bankaccount.Bankaccount(start_balance)
# Внести на счет зарплату пользователя:
    pay = float(input("Сколько вы получили на этой неделе?"))
    print("Вношу эту сумму на ваш счет")
    savings.deposit(pay)
# Показать остаток
    print(savings)
# Получить сумму с банковского счета:
    cash = float(input('Какую сумму желаете снять со счета?'))
    print('Снимаю эту сумму с вашего счета')
    savings.withdraw(cash)
# Показать остаток
    print(savings)


def message():
    my_account = bankaccount.Bankaccount(12234.0)
    mess = str(my_account)
    print(mess)


# Вызвать главную функцию:
if __name__ == '__main__':
    # main()
    message()
