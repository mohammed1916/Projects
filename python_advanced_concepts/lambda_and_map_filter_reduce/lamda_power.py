"""Create a lambda function which takes two inputs X and Y and performs X power Y
operation and returns the output. For Example: If X is 2 and Y is 3, then 2 power 3 = 2
* 2 * 2 = 8."""

power = lambda x,y: x**y

x = int(input("Enter base "))
y = int(input("Enter power "))
print(f'{x} power {y} is {power(x,y)}')