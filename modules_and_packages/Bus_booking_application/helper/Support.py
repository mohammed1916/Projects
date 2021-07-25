"""
Package Helper:
Create a file support.py in this package and the support.py should have class MyHelper. This
MyHelper should have following methods -
    1. print_time() -> prints current time
"""
from datetime import datetime


class MyHelper:
    def print_time():
        print("Current Time: ",datetime.now().strftime("%H:%M:%S"))