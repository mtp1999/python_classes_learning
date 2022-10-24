"""
This section is about multiple inheritance.
it is similar when a child inherits from his parents.
"""


class Parent1:
    def __init__(self, name1):
        self.name1 = name1
        print('In Parent1')


class Parent2:
    def __init__(self, name2):
        self.name2 = name2
        print('In Parent2')


class Child(Parent1, Parent2):
    def __init__(self, name1, name2):
        Parent1.__init__(self, name1)
        Parent2.__init__(self, name2)
        print('In Child')

    def print_names(self):
        return 'name1: {}, name2: {}'.format(self.name1, self.name2)


object1 = Child('Jack', 'Louis')
print(object1.print_names())
