# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hello(self):
#         print(f"Hello! My Name is {self.name}")
#
#     def get_info(self):
#         return f"{self.name}; {self.age}"
#
# vasya = Student("Vasya",15)
# petya = Student("Petya",17)
# print(vasya)
# print(vasya.name,vasya.age)
# print(petya.name,petya.age)
# vasya.say_hello()
# print(vasya.get_info())
# del vasya
# print(vasya.name)

# class Animal:
#     animal_counter = 0
#
#     def __init__(self,animal_type, name):
#         self.animal_type = animal_type
#         self.name = name
#         Animal.animal_counter += 1
#
#     def show_info(self):
#         print(f"{self.animal_type};{self.name}")
#
# print(Animal.animal_counter)
# barsik = Animal("Cat","Barsik")
# sharik = Animal("Dog","Sharik")
# barsik.show_info()
# print(barsik.animal_counter)


# class Car:
#     car_counter = 0
#
#     def __init__(self,brand, model, price):
#         self.brand = brand
#         self.price = price
#         self.model = model
#         Car.car_counter += 1
#
#     def get_info(self):
#         return f"{self.brand}{self.model}. Price: {self.price}"
#
#     @classmethod
#     def get_car_counter(cls):
#         return cls.car_counter
#
#     @staticmethod
#     def song():
#         print("BRRBRBRBRRBR")
#
#     @property
#     def car_price(self):
#         return self.price
#
# m3 = Car("BMW","M3",3_000_000)
# print(m3.get_info())
# print(m3.get_car_counter())
# f40 = Car("Ferrari","F40",30_000_000)
# print(f40.get_car_counter())
#
# print(Car.car_counter)
# print(Car.get_car_counter())
#
# m3.song()
# Car.song()
#
# print(f40.car_price)

# class Passport:
#     passport = 0
#
#     def __init__(self,fio,birthday,pol,id,city):
#         self.fio = fio
#         self.birthday = birthday
#         self.pol = pol
#         self.id = id
#         self.city = city
#
#     def show_info(self):
#          print( f"FIO: {self.fio}\nBirthday: {self.birthday}\nPol: {self.pol}\nid: {self.id}\ncity: {self.city}")
#
# vlad = Passport("Ivanov I.I","23.12.2025","муж","9089455GHVVF","Moscow")
# print(vlad.show_info())


# class Ship:
#     def __init__(self,ship_type, lenght, year):
#         self.ship_type = ship_type
#         self._lenght = lenght
#         self.__year = year
#
#     def set_year(self,value):
#         self.__year = value
#
#     def get_year(self):
#         return self.__year
#
# titanic = Ship("Пароход",400,1909)
# print(titanic.ship_type)
# print(titanic._lenght)
#
# print(titanic.set_year(1910))
# print(titanic.get_year())

# ПОЛИМОРФИЗМ
# class Cat:
#     def __init__(self,name,year):
#         self.name = name
#         self.year = year
#
#     def say(self):
#         print("MEOW!!!!")
#
# class Dog:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def say(self):
#         print("WOWWOW!!!!")
#
# barsik = Cat("Barsik",15)
# sharik = Dog("Sharik",10)
# barsik.say()
# sharik.say()

# Наследование
# class Human:
#     def __init__(self,name,year):
#         self.name = name
#         self.year = year
#
#     def say_hello(self):
#         print(f"Hello! my name is {self.name}")
#
# class Student(Human):
#     def __init__(self,name, yaer, group):
#         super().__init__(name, year)
#         self.group = group


class Weather:

    @staticmethod
    def celsius_to_fahrenheit(t):
        return t * 9/5 + 32

    @staticmethod
    def celsius_to_kelvins(t):
        return t + 235.15

    @staticmethod
    def fahrenheit_to_celsius(t):
        return (t - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvins(t):
        return (t - 32) * 5/9 + 273.15

    @staticmethod
    def kelvins_to_celsius(t):
        return t - 273.15

    @staticmethod
    def kelvins_to_fahrenheit(t):
        return (t - 273.15) * 9/5 + 32


print(Weather.celsius_to_fahrenheit(6))
print(Weather.celsius_to_kelvins(9))
print(Weather.fahrenheit_to_celsius(34))
print(Weather.fahrenheit_to_kelvins(10))
print(Weather.kelvins_to_celsius(9))
print(Weather.kelvins_to_celsius(12))