import math

L = [1,2,3,4]

fact =[math.factorial(num)  for num in L if num%2==0]

print(fact)