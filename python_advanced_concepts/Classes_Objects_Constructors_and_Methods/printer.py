"""
Create a class Printer with a default constructor and a method called print_me(data), which
returns the data that comes as argument.
Example:
Let’s say obj is the object for Printer class.
res = obj.print_me(“Welcome”)
print(res)
Output:
Welcome
"""

class Printer:
    def print_me(self,data):
        return data

obj = Printer()
res = obj.print_me('Welcome')
print(res)

"""
OUTPUT
------

Welcome
"""