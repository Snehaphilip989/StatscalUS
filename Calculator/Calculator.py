from Calculator.Addition import addition
from Calculator.Subtraction import sub
from Calculator.Division import division
from Calculator.Multiplication import multiply
from Calculator.Square import square
from Calculator.sqroot import sqroot



class Calculator:
    result = 0

    def __init__(self):
        pass


    def subtract(self, a, b):
        self.result = sub(a, b)
        return self.result



    def add(self, a, b):
        self.result = addition(a, b)
        return self.result



    def divide(self, a, b):
        self.result = round(division(a, b), 7)
        return self.result



    def square(self, a):
        self.result = square(a)
        return self.result



    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result



    def squareroot(self, a):
        self.result = sqroot(a)
        return self.result

