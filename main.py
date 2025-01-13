class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello! My Name is {self.name}")

    def get_info(self):
        return f"{self.name}; {self.age}"

vasya = Student("Vasya",15)
petya = Student("Petya",17)
print(vasya)
print(vasya.name,vasya.age)
print(petya.name,petya.age)
vasya.say_hello()
print(vasya.get_info())
del vasya
print(vasya.name)

