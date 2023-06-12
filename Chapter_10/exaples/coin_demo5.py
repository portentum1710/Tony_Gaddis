# Эта программа импортирует имитационный модуль
# и создает три экземпляра класса Coin.

import coin


def main():
    # Создать три объекта класса Coin:
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()
    # Показать повернутую вверх сторону каждой монеты.
    print('Вот три монеты у которых эти стороны обращены вверх:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())

    print('Подбрасываю все три монеты...')
    coin1.toss()
    coin2.toss()
    coin3.toss()
    # Показать повернутую вверх сторону каждой монеты.
    print('Вот три монеты у которых эти стороны обращены вверх:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())


if __name__ == '__main__':
    main()