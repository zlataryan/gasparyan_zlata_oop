"""
======================================
1. Создай класс SecureData, который:

имеет атрибут __secret, задаваемый в __init__;
переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
внутри класса доступ к __secret должен работать.
Проверь:
data = SecureData("пароль123")
print(data.__secret)      # ошибка
print(data.get_secret())  # "пароль123"
======================================"""

class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def get_secret(self):
        object.__getattribute__(self, '_SecureData__secret')


    def __getattribute__(self, name):
        if name == '_SecureData__secret':
            raise ValueError( 'Ошибка' )
        return object.__getattribute__(self, name)

data = SecureData("пароль123")
# print(data.__secret)
# print(data.get_secret()) тоже не работает, не поняла как исправить

"""2. Добавь в класс SecureData метод __setattr__,
который запрещает создание любого атрибута с именем token.

Проверь:
data.token = "abc123"  # ❌ AttributeError
data.other = "ok"      # ✅ работает
======================================"""
from datetime import datetime
class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def get_secret(self):
        return self.__secret

    def __getattribute__(self, name):
        print(f"Время обращения к {name}: {datetime.now().strftime('%Y.%m.%d %H:%M:%S')}")
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'token':
            raise AttributeError('Запрет на создание любого атрибута с именем token')
        object.__setattr__(self, name, value)



data = SecureData("dedr")
print(data.get_secret())
# data.token = "abc123"
data.other = "ok"


"""3. Создай класс SafeDict, в котором:

нет атрибута default;
реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
Проверь:
d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"
======================================"""
from datetime import datetime
class SafeDict:
    default = None
    def __getattr__(self, name):
        print(f"Попытка вызова несуществующего атрибута: {datetime.now().strftime('%Y.%m.%d %H:%M:%S')}")
        return "N/A"
    def __delattr__(self, name):
        print(f"Удалён атрибут {name}")
        object.__delattr__(self, name)

d = SafeDict()
print(d.unknown)
d.key = 10
del d.key

"""4. Создай класс Employee с приватными полями __name и __salary.
Добавь @property для поля salary, а также сеттер с валидацией:

зарплата должна быть положительным числом;
если нет — выбрасывать ValueError.
Проверь, что:
e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
e.salary = -100   # ❌ ValueError
======================================"""
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Значение поля salary не может быть меньше 0")
        self.__salary = value

e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
e.salary = -100   # ❌ ValueError


"""5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
и поле реально исчезало.
Проверь:

del e.salary
print(e.__dict__)  # salary нет"""
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Значение поля salary не может быть меньше 0")
        self.__salary = value
    @salary.deleter
    def salary(self):
        print ("Зарплата удалена")
        object.__delattr__(self, "_Employee__salary")


e = Employee("Daniil", 5000)
print(e.salary)
e.salary = 8000
print(e.salary)
# e.salary = -100
# del e.salary
print(e.__dict__)

"""6. Представь, что ты пишешь обёртку над HTML-формой.
Создай класс LoginForm с полем username, которое реализовано через @property.

Логика:
геттер возвращает self._username
сеттер добавляет лог "username изменён"
Проверь, что:
form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # "admin"
======================================"""
class LoginForm:
    def __init__(self):
        self._username = None
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, name):
        print("[LOG] username изменён")
        self._username = name
form = LoginForm()
form.username = "admin"
print(form.username)
"""7. Создай класс Card, где:
поле __number хранит номер карты (строка);
в @property возвращай номер с маской **** **** **** 1234;
в @setter проверяй, что номер состоит из 16 цифр;
в @deleter логируй удаление номера с текущим временем.
Напиши тесты (через assert)
проверку установки корректного номера;
проверку исключения при вводе короткого номера;
проверку вывода замаскированного номера.
# ======================================"""
from datetime import datetime
class Card:
    def __init__(self, number: str = None):
        self.__number = number

    @property
    def number(self):
        end = self.__number[-4:]
        return f"**** **** **** {end}"

    @number.setter
    def number(self, value:str):
        if not isinstance(value, str):
            raise TypeError("Номер должен быть строкой")
        if len(value) != 16:
            raise ValueError("Ошибка! Длина номера должна составлять 16 символов")
        self.__number = value

    @number.deleter
    def number(self):
        print(f"[LOG] Удаление объекта. Время: {datetime.now().strftime('%Y.%m.%d %H:%M:%S')}")
        object.__delattr__(self, "_Card__number")

card = Card()
card.number = "8765876587658765"
assert card._Card__number == "8765876587658765", "Установлен некорректный номер"

assert len(card._Card__number) >= 16, "Введен короткий номер"
assert card.number == "**** **** **** 8765", "Ошибка маскировки"

"""8. Создай класс UserData для API регистрации пользователя:
email — строка, содержит @;
age — целое число ≥ 18;
is_active — bool;
свойство .json возвращает словарь для запроса.
Напиши тест (через assert)
проверь, что при age = 15 выбрасывается ValueError;
проверь, что email без @ вызывает ошибку;
проверь, что json возвращает корректную структуру."""

class UserData:
    def __init__(self,
                 email: str,
                 age: int,
                 is_active: bool):
        self.email = email
        self.age = age
        self.is_active = is_active

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, name):
        if not isinstance(name, str):
            raise TypeError("Email должен быть строкой")
        if "@" not in name:
            raise TypeError("Email должен содержать '@'")
        self._email = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Значение возраста может быть только целым числом")
        if value < 18:
            raise ValueError("Значение возраста не может быть меньше 18")
        self._age = value

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value) -> None:
        if not isinstance(value, bool):
            raise ValueError("Значение должно быть True / False")
        self._is_active = value

    @property
    def json(self):
        return {
            "email": self._email,
            "age": self._age,
            "is_active": self._is_active
        }

user = UserData("zl@mail.com",
                30,
                True)
assert user.age == 30, "ValueError"
assert "@" in user.email, "Email не содержит '@'"
assert user.json == {
            "email": "zl@mail.com",
            "age": 30,
            "is_active": True
        }, "Неверная структура json"

