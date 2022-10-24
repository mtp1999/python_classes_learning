"""
This section is about polymorphism.
Polymorphism includes both overriding and overloading.
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def function(self):
        return self.name


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    # override the function
    def function(self):
        return 'Hi im a child!!!'


child1 = Child('Jack')
print(child1.function())