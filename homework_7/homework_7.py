"""
======================================
1. Создай три класса: Cat, Dog, Duck.
В каждом реализуй метод speak(), возвращающий уникальную строку.
Создай список из экземпляров этих классов и вызови метод speak()
в цикле.
======================================"""
class Cat:
    def speak(self):
        return "мяу"

class Dog:
    def speak(self):
        return "гав"

class Duck:
    def speak(self):
        return "кря"

animal = [Cat(), Dog(), Duck()]
res = []
for items in animal:
    res.append(items.speak())
print(res)

"""2. Создай базовый класс Shape
Создай три класса-наследника: Square, Rectangle, Triangle,
в каждом реализуй метод get_pr().
Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
можно обойти в цикле и вызвать get_pr() у каждого.
======================================"""
# class Shape:
#     pass
#
# class Square(Shape):
#     def __init__(self, value):
#         self.value = value
#     def get_pr(self):
#         return self.value * 4
#
#
# class Rectangle(Shape):
#
#     def __init__(self, side_1, side_2):
#         self.side_1 = side_1
#         self.side_2 = side_2
#
#     def get_pr(self):
#         return 2 * (self.side_1 + self.side_2)
#
# class Triangle(Shape):
#     def __init__(self, side_a, side_b, side_c):
#         self.side_a = side_a
#         self.side_b = side_b
#         self.side_c = side_c
#
#     def get_pr(self):
#         return self.side_a + self.side_b + self.side_c
#
# shapes = [Square(2), Rectangle(4, 6), Triangle(10, 1,5)]
# for shape in shapes:
#     print(shape.get_pr())

# """3. Сделай класс Shape абстрактным.
# Переопредели get_pr() как @abstractmethod.
# Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
# ======================================"""
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_pr(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, value):
#         self.value = value
#     def get_pr(self):
#         return self.value * 4
#
#
# class Rectangle(Shape):
#
#     def __init__(self, side_1, side_2):
#         self.side_1 = side_1
#         self.side_2 = side_2
#
#     def get_pr(self):
#         return 2 * (self.side_1 + self.side_2)
#
# class Triangle(Shape):
#     def __init__(self, side_a, side_b, side_c):
#         self.side_a = side_a
#         self.side_b = side_b
#         self.side_c = side_c
#
#     def get_pr(self):
#         return self.side_a + self.side_b + self.side_c
#
#
# shapes = Shape(3) #TypeError


"""4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.
======================================"""
class A:
    def __init__(self):
        super().__init__()
        print("init A")

class B:
    def __init__(self):
        super().__init__()
        print("init B")

class C:
    def __init__(self):
        super().__init__()
        print("init C")

class D(A, B, C):
    def __init__(self):
        print("init D")

print(D.__mro__) # D -> A -> B -> C

"""5. Создай MixinLog (как в уроке).
Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
Создай класс, который наследует оба класса. Создай экземпляр этого класса.
======================================"""
# from datetime import datetime
#
# class MixinLog:
#     ID = 0
#     def __init__(self):
#         print('init MixinLog')
#
#         MixinLog.ID += 1
#
#     def save_sell_log(self):
#         print(f"{self.ID} продан в {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#
# class HotelBooking():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__()
#
#     def guest_info(self):
#         print(f' Имя гостя: {self.name}, Возраст гостя: {self.age}')
#
# class Order(HotelBooking, MixinLog):
#     pass
#
#
# guest_1 = Order("Paul", 18)
# guest_1.guest_info()
# guest_1.save_sell_log()
# #guest_1.save_sell_log()
#
# """6. В Goods и MixinLog реализуй print_info().
# Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
# Измени порядок наследования — изменилась ли логика?
# ======================================"""
# import datetime
#
# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("init Goods")
#
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.price}, {self.weight}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#
#         print("init MixinLog")
#
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#         super().__init__(a, b, d)
#
#     def save_sell_log(self):
#         print(f"{self.id} продан в {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#
#     def print_info(self):
#         print("MixinLog information")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
# n = Notebook("Acer", 1.5, 50_000)
# n.print_info() # ошибка
# # если Goods первый, то супер инит прописывается в гудс и все отрабатывает, а если MixinLog первый,
# # то чтобы передавать в него эти три аргумента ("Acer", 1.5, 50_000), нужно прописывать супер в нем,
# # и в таком случае первый вариант не работает.


"""======================================
Далее задания можете сделать через классы, функции или без них.
======================================
======================================
7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
и выведи сообщение: "На ноль делить нельзя!"
======================================"""
# try:
#     a = float(input())
#     b = float(input())
#     result = a/b
#     print(result)
#
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")

"""8. Расширь программу из Задания 1:
Добавь обработку ошибки (как называется ошибка найди сам),
если пользователь ввёл не числа, а текст.
Выведи сообщение: "Ошибка ввода: введите два числа через пробел"
======================================"""
# try:
#     a = float(input())
#     b = float(input())
#     result = a/b
#     print(result)
#
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# except ValueError:
#     print("Ошибка ввода: введите два числа через пробел")

"""9. Модифицируй код так, чтобы после обработки конкретных ошибок
был ещё один общий except, который перехватывает все остальные ошибки и выводит:
"Произошла неизвестная ошибка"
======================================"""
# try:
#     a = float(input())
#     b = float(input())
#     result = a/b
#     print(result)
#
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# except ValueError:
#     print("Ошибка ввода: введите два числа через пробел")
# except Exception:
#     print("Произошла неизвестная ошибка")

"""10. При перехвате исключений из 7 и 8 заданий,
сохрани ошибку в переменную e и выведи её текст:
======================================"""
# try:
#     a = float(input())
#     b = float(input())
#     result = a/b
#     print(result)
#
# except ZeroDivisionError as e:
#     print(f"Ошибка: {e}")
#     print("На ноль делить нельзя!")
# except ValueError as e:
#     print(f"Ошибка: {e}")
#     print("Ошибка ввода: введите два числа через пробел")
# except Exception:
#     print("Произошла неизвестная ошибка")

"""11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.
======================================"""
# try:
#     a = float(input())
#     b = float(input())
#     result = a/b
#     print(result**1000000000002)
#
# except ArithmeticError as e:
#     print(f"Ошибка: {e}")
#     print("Арифметическая ошибка")

"""12. Запроси у пользователя два числа и выполни деление.
Если деление прошло успешно без ошибок — выведи
"Деление выполнено успешно" через (но не в блоке try)
======================================"""
# try:
#     a = float(input())
#     b = float(input())
#     result = a/b
#
# except ZeroDivisionError as e:
#     print(f"Ошибка: {e}")
#     print("На ноль делить нельзя!")
# except ValueError as e:
#     print(f"Ошибка: {e}")
#     print("Ошибка ввода: введите два числа через пробел")
# except Exception:
#     print("Произошла неизвестная ошибка")
# else:
#     print("Деление выполнено успешно")


"""13. Расширь код из Задания 12:
Добавь блок, в котором будет выводиться
"Работа программы завершена", независимо от успеха деления.

======================================"""
# try:
#     a = float(input())
#     b = float(input())
#     result = a/b
#
# except ZeroDivisionError as e:
#     print(f"Ошибка: {e}")
#     print("На ноль делить нельзя!")
# except ValueError as e:
#     print(f"Ошибка: {e}")
#     print("Ошибка ввода: введите два числа через пробел")
# except Exception:
#     print("Произошла неизвестная ошибка")
# else:
#     print("Деление выполнено успешно")
# finally:
#     print("Работа программы завершена")

"""14. Реализуй две вложенные конструкции:
Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
Внутренний try/except ловит деление на ноль.
======================================"""
# try:
#     try:
#         a = int(input())
#         b = int(input())
#         res = a/b
#     except ZeroDivisionError as e:
#         print(f"Ошибка: {e}")
#
# except ValueError as e:
#     print(f"Ошибка ввода: {e}\nВведите два числа через пробел")


"""15. Вынеси обработку деления в отдельную функцию divide(x, y)
с собственным try/except.
Во внешнем коде обработай только ошибку ввода.
"""

def divide(x, y):
    try:
        x / y
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
try:
    x = int(input())
    y = int(input())
    divide(x, y)

except ValueError as e:
    print(f"Ошибка ввода: {e}\nВведите два числа через пробел")