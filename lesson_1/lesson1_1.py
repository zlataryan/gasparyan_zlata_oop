"""
++++++++++++++++++++++++++++++++++++++
Классы и атрибуты
++++++++++++++++++++++++++++++++++++++
======================================
1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
Проверь, как это повлияло на значения у обоих объектов.
Убедись, что __dict__ объектов отражает изменения."""

class Dog:
    species = "canis"
    legs = 4
Mike = Dog()
Bobik = Dog()

Mike.legs = 2

print("колличество ног у Майка:", Mike.legs)
print(Mike.legs)
print(Mike.__dict__)
# =========================================================================
"""2. Добавь в класс Dog строку документации, описывающую его назначение.
Затем выведи её на экран.
После этого добавь в объект класса новые атрибуты name и age,
а затем удали name.
Проверь, что произойдёт при попытке снова вывести объект.name."""
class Dog:
    "Описание собочьих особенностей"
    species = "canis"
    legs = 4
spits = Dog()
korgie = Dog()

print(Dog.__doc__)

setattr(korgie, "name", "Bobik")
setattr(korgie, "age", 5)
print("имя собаки: ", getattr(korgie, "name"),"\n","возраст: ", (getattr(korgie, "age")))

delattr(korgie, "name")

print("имя собаки: ", getattr(korgie, "name"),"\n","возраст: ", (getattr(korgie, "age")))
# print(getattr(korgie, "age"))

# =========================================================================
"""3. Создай класс User с атрибутами класса role = "guest" и active = True.
С помощью функций getattr(), setattr(), hasattr() и delattr():

измени значение role на "admin",
проверь наличие active,
добавь новый атрибут email,
удали role.
Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.
"""
class User:
    role = "guest"
    active = True
setattr(User, "role", "admin")

print(hasattr(User, "active"))

setattr(User, "email", 0)

delattr(User, "role")

print(User.__dict__)