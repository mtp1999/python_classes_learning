"""
This section is about some other useful decorators.
like @property, @functionName.setter, @functionName.deleter
"""
class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        # self.mail = first_name + '.' + last_name + '@company.com'
        # in this mail,if later there is change in first or last,
        # there is no change in mail and its not good.

    @property  # it makes method become an attribute
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None

    @property
    def mail(self):
        if self.first_name is not None and self.last_name is not None:
            return self.first_name + '.' + self.last_name + '@company.com'
        else:
            return None

    # Not equal
    def __ne__(self, other):
        if self.pay != other.pay:
            return True


e1 = Employee('Jack', 'Sparrow', 4000)
print(e1.mail)
e1 = Employee('Johnny', 'Cage', 4000)
print(e1.mail)

e1.full_name = 'Leonardo Dicaprio'
print(e1.mail, e1.first_name, e1.last_name)


e2 = Employee('Jane', 'Queens', '3000')

print(e2 != e1)

del e1.full_name
print(e1.mail, e1.first_name, e1.last_name)
