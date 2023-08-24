class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(self.brand, self.year)


class Automobile(Vehicle):
    def __init__(self, engine, type_of_vehicle, brand, year):
        super().__init__(brand, year)
        self.engine = engine
        self.type_of_vehicle = type_of_vehicle

    def display_info(self):
        print(self.year, self.brand, self.engine, self.type_of_vehicle)


class Motorbike(Vehicle):
    def __init__(self, brand, year, weight, moto_engine):
        super().__init__(brand, year)
        self.weight = weight
        self.moto_engine = moto_engine

    def display_info(self):
        print(self.year, self.brand, self.weight, self.moto_engine)



while True:
    a = input('опции: auto, bike, year_and_brand_______')
    if a.lower() == 'auto':
        auto_mechanic = Automobile(year = int(input('введите год: ')), brand = input('брэнд машины: '), engine = input('двигатель мащины: '), type_of_vehicle = input('тип машины: '))
        auto_mechanic.display_info()

    elif a.lower() == 'bike':
        auto_mechanic = Motorbike(year = int(input('введите год: ')), brand = input('брэнд байка: '), moto_engine = input('двигатель байка: '), weight = input('вес байка: '))
        auto_mechanic.display_info()

    elif a.lower() == 'just_info':
        auto_mechanic = Vehicle(year = int(input('введите год: ')), brand = input('введите марку: '))
        auto_mechanic.display_info()
    else:
        print('ERROR')



