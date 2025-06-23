# Магические, статичные, классовые методы в классах, множественное наследование.


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"Точкa {self.x}, {self.y}"

#     def __add__(self, other):
#         if isinstance(other, Point):
#             return Point(self.x + other.x, self.y + other.y)
#         return NotImplemented

#     def __eq__(self, other):
#         return self.x == other.x, self.y == other.y

# p1 = Point(1, 2)
# p2 = Point(3, 4)

# # print(p1)
# # print(p2)

# p3 = p1 + p2
# print(p3)

# print(p1 == p2)
# print(p1 == Point(1,2))


# class Converter:
#     @staticmethod
#     def selsius_tofahrenheit(celsius):
#         return celsius * 9 / 5 + 32

#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5 / 9

# print(Converter.selsius_tofahrenheit(0))
# print(Converter.fahrenheit_to_celsius(212))

# class Test:
#     value = 10 

#     @staticmethod
#     def static_show():
#         # print(self.value)  В статичном методе нет self или cls
#         # print(cls.values)
#         print("Это статичный метод, нет доступа к селф и клс")

# print(Test.static_show())


# class Person:
#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def from_fullname(cls, fullname):
#         name = fullname.split()[0]
#         return cls(name)

# p = Person.from_fullname("Ivan Ivanovich")
# print(p.name)

# class Demo:
#     class_attr = "Class"
# 
#     def instance_method(self):
#         print(f"Обычный метод self = {self}")
# 
#     @classmethod
#     def class_method(cls):
#         print(f"Классовый метод cls = {cls}")
# 
#     @staticmethod
#     def static_method():
#         print("Статичный метод")
# n
# ojb = Demo()
# ojb.instance_method()
# ojb.class_method()
# ojb.static_method()

# class A:
#     def greet(self):
#         print("class from A")
# 
# class B:
#     def greet(self):
#         print("class from B")
# 
# class C(A,B):
#     def greet(self):
#         B.greet(self)
#         A.greet(self)
# 
# c = C()
# c.greet()
# print(C.mro())