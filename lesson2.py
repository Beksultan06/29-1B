

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
# 
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"{amount} успешно зачислено")
#         else:
#             print("Нельзя внести отрицательную сумму")
# 
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{amount} снято")
#         else:
#             print("Недостаточно средст")
# 
#     def get_balance(self):
#         return self.__balance
# 
# account = BankAccount("Bob", 2000)
# 
# print(account.owner)
# # print(account.balance)
# # print(account.get_balance())
# 
# print(account._BankAccount__balance)
# 
# account.__balance = -10000\


# class Car:
#     def __init__(self, brand, model, engine_number):
#         self.brand = brand      # публичный
#         self._model = model     # защищенный 
#         self.__engine_number = engine_number    # приватный

#     def show_info(self):
#         print(f"Марка : {self.brand}")
#         print(f"Модель {self._model}")
#         print(f"Номер двигателя {self.__engine_number}")


# car = Car("Toyota", "Carolla", "END1231421")

# print(car.brand)
# print(car._model)

# try:
#     print(car.__engine_number)
# except AttributeError:
#     print("Нельзя получить доступ к__engine_number напрямую ")

# car.show_info()


# class Car:
#     def __init__(self, brand, model, engine_number):
#         self.brand = brand      # публичный
#         self._model = model     # защищенный 
#         self.__engine_number = engine_number    # приватны
# 
#     # getter engine_number
#     @property
#     def engine_number(self):
#         return self.__engine_number
# 
#     @engine_number.setter
#     def engine_number(self, value):
#         if isinstance(value, str) and value.startswith("ENG"):
#             self.__engine_number = value
#         else:
#             print("Неверный формат номера двигателя")
# 
#     @property
#     def model(self):
#         return self._model
# 
#     @model.setter
#     def model(self, value):
#         if value:
#             self._model = value
#         else:
#             print("Модел не должен быть пустым")
# 
# car = Car("BMW", "X5", "ENG23124124")
# 
# print(car.brand)
# 
# print("Model: ", car.model)
# car.model = "M5"
# print("Model: ", car.model)
# 
# print("Engine number:", car.engine_number)
# car.engine_number = "ENG111111"
# print("Engine number:", car.engine_number)
# # car.engine_number = "BMW111111"
# # print("Engine number:", car.engine_number)
# 
# 

# class Animal:
#     def speak(self):
#         print("Животне издает звук")
# 
# class Dog(Animal):
#     def speak(self):
#         print("Собака лает")
# 
# class Cat(Animal):
#     def speak(self):
#         print("Кошка мяукает")
# 
# animals = [Dog(), Cat(), Animal()]
# 
# for animal in animals:
#     animal.speak()
# 
# print(animals.speak())


# 🧠 Задание: "Система Уведомлений"
# Создай абстрактный класс Notification, у которого будет метод send().
# А затем создай три подкласса, которые реализуют этот метод по-своему:
# EmailNotification – отправка письма.
# SMSNotification – отправка СМС.
# PushNotification – отправка push-уведомления на телефон.
# 🔧 Что нужно сделать:
# Создай класс Notification с методом send(), 
# который просто печатает "Уведомление отправлено" (или сделай pass).
# В каждом подклассе переопредели send():
# EmailNotification: выводит "Отправлено письмо на email".
# SMSNotification: выводит "Отправлено SMS-сообщение".
# PushNotification: выводит "Отправлено push-уведомление".
# Создай список из разных типов уведомлений.
# Пройди по ним в цикле и вызови .send() — чтобы полиморфизм сработал.