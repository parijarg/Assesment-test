from abc import ABC, abstractmethod


class mathematical_operation():
    @abstractmethod
    def process(self):
        pass


class add():

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def process(self):
        try:
            return (self.val1 + self.val2)
        except Exception as e:
            print(e)


class subtract():

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def process(self):
        try:
            return (self.val1 - self.val2)
        except Exception as e:
            print(e)


class multiply():

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def process(self):
        try:
            return (self.val1 * self.val2)
        except Exception as e:
            print(e)


class divide():

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def process(self):
        try:
            return (self.val1 / self.val2)
        except Exception as e:
            print(e)


a = int(input("enter first number: "))
b = int(input("enter second number: "))
addition = add(a, b)
substraction = subtract(a, b)
multiplication = multiply(a, b)
division = divide(a, b)

print('addition of first and second value is', addition.process())
print('Substraction of first and second value is', substraction.process())
print('Multiplication of first and second value is', multiplication.process())
print('Division of first and second value is', division.process())
