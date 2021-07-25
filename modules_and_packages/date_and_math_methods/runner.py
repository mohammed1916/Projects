"""
Create another file runner.py and import DateOperations and MathOperations classes and
call the methods get_current_date, get_square_root and get_power_val.
"""

from modules_and_packages.date_and_math_methods.date_and_math import DateOperations,MathOperations

print(DateOperations.get_current_date())
print(MathOperations.get_square_root(16))
print(MathOperations.get_power_val(3,2))

"""
Sample Output:
25/7/2021
4.0
9.0
"""