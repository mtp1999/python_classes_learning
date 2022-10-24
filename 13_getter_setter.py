"""
This section is about getter and setter.
"""


class Person:
    id_counter = 0

    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__code = None

    @property
    def id(self):
        if self.__code is None:
            Person.id_counter += 1
            self.__code = Person.id_counter
        return self.__code

    # getter
    def return_age(self):
        return self._age

    # setter
    def change_id(self, id):
        self.__code = id
        return self.__code


p1 = Person('mtp', 40)
print(p1.return_age())
print(p1.change_id(7))
print(p1.id)
