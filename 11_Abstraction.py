"""
This section is about abstract base class.
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self):
        self.var = 1

    @abstractmethod
    def payment(self):
        pass


class Developer(Payment):
    def __init__(self, name, lang):
        super().__init__()
        self.name = name
        self.lang = lang
        self.pay = self.payment()

    def payment(self):
        if self.lang == 'python':
            return 5000
        else:
            return 4000


d1 = Developer('Jack sparrow', 'java')
print(d1.var)
print(d1.pay)

d1.lang = 'python'
print(d1.pay)

