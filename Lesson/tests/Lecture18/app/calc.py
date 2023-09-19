from math import sqrt,pow

class Calculator:

def division(self, a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def mult(self, a, b):
    return a * b

def subtract(self, a, b):
    return a - b

def power(self, a, b):
    return a ** b

def square_root(self, a):
    if a < 0:
        raise ValueError("Square root of a negative number is not allowed.")
    return a ** 0.5


