"""
======================================
1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
Создай два объекта и задай им разные значения. Выведи информацию по каждому.
======================================"""
class Person:
    def set_data(self, name, age):
        self.name = name
        self.age = age
        print("установка имени и возраста")

    def get_data(self):
        return(f"Имя: {self.name}, Возраст: {self.age}")

pers_1 = Person()
pers_2 = Person()
pers_1.set_data( "Ann", 18)
pers_2.set_data( "Bob", 40)

print(pers_1.get_data())

"""2. Добавь в класс Point методы set_coords(x, y) и get_coords().
Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
После этого измени координаты на (-3, 5) и снова выведи результат через get_coords().
# ======================================"""
class Point:
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

p = Point()
p.set_coords(7, 12)
print(p.get_coords())
p.set_coords(-3, 5)
print(p.get_coords())

"""3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
Проверь, что результат совпадает с обычным вызовом p.get_coords().
======================================"""
Coords = getattr(p, "get_coords")
print(Coords())

"""4. Создай класс Person, в котором метод __init__() принимает имя и возраст и сохраняет их как атрибуты объекта.
Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод.
======================================"""
class Person:
    def __init__(self, name, age: int):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Имя: {self.name}, возраст: {self.age}")
student = Person('Ann', 18)
student.show_info()


"""5. Добавь в класс Person метод __del__(), который выводит сообщение "Удалён объект: <имя>",
где <имя> — значение поля name. Создай и удали объект вручную с помощью del.
======================================"""
class Person:
    def __init__(self, name, age: int):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Имя: {self.name}, возраст: {self.age}")
    def __del__(self):
        print(f"Удалён объект: {self.name}")

student = Person('Ann', 18)
student.show_info()
del student

"""6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
Добавь метод area(), который возвращает площадь прямоугольника.
Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой.
# ======================================"""
class Rectangle:
    length = 1
    width = 1
    def area(self):
        return self.length * self.width
a = Rectangle()
print(a.area())




"""7. Создай класс Logger, который всегда возвращает один и тот же объект.
При создании экземпляра в __new__ выводи Создание логгера,
а при вызове __init__ — Инициализация логгера.
======================================
"""
class Logger:
    instanse = None
    def __new__(cls):
        print("Создание логгера")
        if cls.instanse == None:
            cls.instanse = super().__new__(cls)
        return cls.instanse
    def __init__(self):
        self.zn = []
        print("Инициализация логгера")

name_1 = Logger()
name_2 = Logger()
print(id(name_1))
print(id(name_2))