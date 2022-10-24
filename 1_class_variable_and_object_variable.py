"""
We can access to a class variable with both self and class_name.
when we wanna access to a variable by an object, if the object has this variable,
give us the value of it.But if the object doesnt have it, it search in class variables
to find it.
"""


class Employee:
    pay_rising = 0.1

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.mail = first_name + '.' + last_name + '@company.com'

    def full_name(self):
        print('{} {}'.format(self.first_name, self.last_name))

    def pay_increase(self):
        self.pay += int(self.pay * Employee.pay_rising)


emp1 = Employee(first_name='Jack', last_name='bing', pay=2000)
emp2 = Employee('Louis', 'lenon', 3000)

print(emp1.pay_rising)
print(emp2.pay_rising)
print(Employee.pay_rising)

emp1.pay_rising = 0.2

print('after changing')

print(emp1.pay_rising)
print(emp2.pay_rising)
print(Employee.pay_rising)

# __dict__ shows a dictionary that includes information about the object.
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)
