"""
Create a python class DateOperations with following methods Hint: Use Datetime module
    1. get_current_date() -> This function should return today’s date in format DD/MM/
        YYYY. Example: 18/03/1994.
Create a python class MathOperations with following methods Hint: Use math module
    1. get_square_root(no) -> This function should return square root of given number
    2. get_power_val(x,y) -> The function should return X power Y as output. 
    (Example: X=3, Y=2 , then 3 power 2 => 3 * 3 = 9)

Create another file runner.py and import DateOperations and MathOperations classes and
call the methods get_current_date, get_square_root and get_power_val.
"""

import datetime,math

class DateOperations:
    def get_current_date():
        now = datetime.date.today()
        return str(now.day)+"/"+str(now.month)+"/"+str(now.year)

class MathOperations:
    def get_square_root(no):
        return(math.sqrt(no))

    def get_power_val(x,y):
        return(math.pow(x,y))

