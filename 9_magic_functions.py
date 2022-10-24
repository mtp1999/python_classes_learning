"""
In this section we used some of magic functions.
"""

# print(1 + 2 + 3)
# print(int.__add__(1,int.__add__(2,3)))


class Person:
    id = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.id += 1
        self.id = Person.id

    def __add__(self, other):
        return self.age + other.age

    def __repr__(self):  # print this function for seeing information of an object (special for developers)
        return __class__.__name__ + ' {} : {} {}'.format(self.id, self.first_name, self.last_name)

    def __str__(self):  # print this function for seeing information of an object
        return __class__.__name__ + ' {} : {} {}'.format(self.id, self.first_name, self.last_name)


p1 = Person('Jack', 'Grilish', 45)
p2 = Person('Andres', 'Song', 21)
print(p1.__add__(p2))
print(p1.__repr__(), p2.__repr__())
print(p1.__str__(), p2.__str__())
print(p1.age)