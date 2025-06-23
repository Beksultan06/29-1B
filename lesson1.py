

# class Dog:
#     pass

# dog1 = Dog() # Объект на основе класса Dog
# dog2 = Dog() # Объект на основе класса Dog


# num = []
# print(num)

# Функция внутри класса это уже методы

# class Dog:
#     # Конструтор (инициализация объектов)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def bark(self):
#         print(f"{self.name} говорит: Гав")
# 
#     def age(self):
#         return self.age
# 
# dog1 = Dog("Bob", 5)
# print(dog1.bark())
# print(dog1.name)
# dog1.bark()
# print(dog1.age)


# Принцип ООП - Наследование 

# Родительский класс 
# class Animal:
#     def __init__(self, name):
#         self.name = name
# 
#     def speak(Self):
#         print(f"{Self.name} издает звук")
# 
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} издает May")
# 
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} издает Gav")
# 
# cat = Cat("Мурка")
# dog = Dog("Bob")
# 
# cat.speak()
# dog.speak()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Првиет меня зовут {self.name} мне {self.age} лет")

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def introduce(self):
        super().introduce()
        print(f"Я учусь в {self.university}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"Я преподаю предмет {self.subject}")

student = Student("Алина", 19, "МГУ")
student.introduce()
teacher = Teacher("Атон Иванович", 45, "Python ML")
teacher.introduce()