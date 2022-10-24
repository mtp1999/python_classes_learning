"""
This section is about multi level inheritance.
son class inherits from father class and
father class inherits from grandpa class.
"""


class Grandpa:
    def __init__(self):
        self.attr1 = 'Kindness'


class Pa(Grandpa):
    def __init__(self):
        Grandpa.__init__(self)
        self.attr2 = 'Savage'


class Son(Pa):
    def __init__(self):
        Pa.__init__(self)
        self.attr3 = 'sadness'

    def print_attrs(self):
        print(self.attr1, self.attr2, self.attr3)


son1 = Son()
son1.print_attrs()
