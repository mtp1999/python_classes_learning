"""
In this section you can understand the difference between instance_method,
class_method and static_method.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method_calculate_age(cls, name, birthdate):  # class method that can return an object
        import datetime
        return cls(name, datetime.date.today().year - birthdate)

    @staticmethod
    def static_method_adult(age):  # static method
        if age >= 18:
            return True
        else:
            return False


person1 = Person.class_method_calculate_age('Jack', 1988)
print('Person1 age :', person1.age)
print('Is he adult?', person1.static_method_adult(person1.age))


class Employee:
    pay_rising = 0.1

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.mail = first_name + '.' + last_name + '@company.com'

    def full_name(self):  # instance method
        return '{} {}'.format(self.first_name, self.last_name)

    def pay_increase(self):
        self.pay += int(self.pay * self.pay_rising)

    @classmethod
    def class_method_change_pay_rising(cls, amount):
        cls.pay_rising = amount

    @classmethod
    def class_method_make_instance_by_string(cls, string):  # make instance with class method
        first, last, pay = string.split('-')
        return cls(first, last, int(pay))


emp1 = Employee(first_name='Louis', last_name='Lillard', pay=2000)
emp2 = Employee('Samuel', 'James', 3000)
make_emp3 = 'Jimmy-Leonard-4000'
emp3 = Employee.class_method_make_instance_by_string(make_emp3)

print(emp1.full_name())
print(emp2.full_name())
print(emp3.full_name())


# both bottom lines can change a variable class
# emp1.__class__.pay_rising = 0.2
# Employee.pay_rising = 0.2
