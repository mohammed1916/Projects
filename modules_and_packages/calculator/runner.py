"""
Create a python module calculator.py with class Calculator. The calculator class should have
functions add(x,y), sub(x,y), mul(x,y), div(x,y). Create another file python runner.py and import
calculator module here and call add, sub, mul and div functions.
"""

from modules_and_packages.calculator.calculator import Calculator

print(Calculator.add(10,10))
print(Calculator.sub(30,20))
print(Calculator.mul(2,5))
print(Calculator.div(10,5))

"""
OUTPUT:
20
10
10
2
"""
