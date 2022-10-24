"""
This section is about public, protected and private variables.
"""


class Class1:
    def __init__(self):
        self.a = 10  # public
        self._b = 20  # protected
        self.__c = 30  # private


object1 = Class1()
print(object1.a)
print(object1._b)
# print(o1.__c)    # raise error
print(dir(object1))
print(object1._Class1__c)  # for access to c


