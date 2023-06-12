import pickle
import retail_item
FILENAME = "retail.dat"


def main():
    input_file = open(FILENAME, 'rb')
    # flag to stop
    end_of_file = False

    count_retail = 1
    while not end_of_file:
        try:
            item = pickle.load(input_file)
            desplay_item(item, count_retail)
            count_retail += 1

        except EOFError:
            end_of_file = True


def desplay_item(item, count):
    print(f'Товар номер {count}')
    print(f'Наименование товара: {item.get_name()}')
    print(f'Кол-во товара: {item.get_quantity()}')
    print(f'Цена товара: {item.get_price()}')
    print('----------------------')

if __name__ == '__main__':
    main()