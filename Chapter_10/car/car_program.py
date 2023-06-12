import car_class


def main():
    year_model = input('Specify car model: ')
    make = input('Specify manufacturer: ')
    car = car_class.Car(year_model, make)

    for count in range(5):
        car.accelerate()
        print(car.get_speed())

    for count in range(5):
        car.to_break()
        print(car.get_speed())


if __name__ == '__main__':
    main()
