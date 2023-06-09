# Это программа импортирует модуль coin
# и создает экземпляр класса Coin

import coin


def main():
      # создать объект на основе класса Coin
      my_coin = coin.Coin()

      print(my_coin.get_sideup())

      print("Собираюсь подбросить монету 10 раз:")
      for count in range(10):
          my_coin.toss()
          print(my_coin.get_sideup())

if __name__ == '__main__':
    main()
