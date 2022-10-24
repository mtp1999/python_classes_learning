"""
This section is about single inheritance.
"""


class Person:

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def person_introduction(self):
        return 'Name is {} with id:{}'.format(self.name, self.id_number)


class Employee(Person):

    def __init__(self, name, id_number, job):
        Person.__init__(self, name, id_number)
        self.job = job

    def employee_introduction(self):
        return 'employee name is {} with id:{} and his/her job is {}.'.format(self.name, self.id_number, self.job)


emp1 = Employee('Michael Cool', 1113, 'developer')
print(emp1.employee_introduction())
