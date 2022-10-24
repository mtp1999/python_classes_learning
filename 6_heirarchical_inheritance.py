"""
This section is about heirarchical inheritance.
child classes inherit from a parent class
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


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        # Employee.__init__(self,first_name,last_name,pay)
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee_for_manager(self, employee):
        self.employees.append(employee)

    def remove_employee_for_manager(self, employee):
        self.employees.remove(employee)

    def show_employees_of_manager(self):
        for e in self.employees:
            e.full_name()


class Developer(Employee):
    def __init__(self, first_name, last_name, pay, program_language):
        Employee.__init__(self, first_name, last_name, pay)
        self.program_language = program_language


m1 = Manager('Jack', 'Grilish', 8000)
d1 = Developer('Samuel', 'Jackson', 4000, 'java')
m1.add_employee_for_manager(d1)

m1.show_employees_of_manager()

print(isinstance(m1, Manager))
print(issubclass(Manager, Employee))

# mro = method resolution order
print(Manager.__mro__)
