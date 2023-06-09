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
    print(f'Ваш остаток на счете составляет: ${savings.get_balance():.2f}')


if __name__ == '__main__':
    main()
