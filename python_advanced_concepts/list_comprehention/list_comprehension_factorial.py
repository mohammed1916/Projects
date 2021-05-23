"""Write a list comprehension to find factorial of each numbers in a given list L if and only
if the numbers are even. For Example: If L = [1,2,3,4] then output should be [2, 24]."""

import math

L = [1,2,3,4]

fact =[math.factorial(num)  for num in L if num%2==0]

print(fact)