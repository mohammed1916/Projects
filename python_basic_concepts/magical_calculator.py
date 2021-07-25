"""You are going to design a magical calculator with the following functions.
• Function that takes input and calculates it’s factorial. (A)
• Function that takes input and calculate it’s sum of digits. (B)
• Function that takes input and find’s the largest digit in the input. (C)
- Implement all the above functions.
- Get input and pass the input to factorial function (A), get the output from
factorial function and pass it as input to sum of digits function (B). Get the output
from sum of digits function, add the output with random 5 digit number and pass
the outcome to largest digit function (C) and print the output that you receive from
function C.
Sample I/O:
• Input 5
• Output of A = 120
• Output of B(120) = 1+2+0 = 3
• Output of C(3 + 10000 = 10003) = 3 (Here 10000 is the random number)
• Hence output is 3 , where 3 is the largest digit of 10003."""

import random

def A(number):
    fact=1
    while(number>1):
        fact = fact *number
        number-=1
    return fact

def B(number):
    number=str(number)
    total=0
    for digit in number:
        total=total+int(digit)
    return total

def C(number):
    number=str(number)
    digit_contents=[]
    for digit in number:
        digit_contents.append(int(digit))
    return max(digit_contents)

number = int(input('Enter number: '))

random_num = random.randint(0,100000)
fact_num = A(number)
sum_fact = B(fact_num)
largest_digit = C(sum_fact + random_num)

print(largest_digit)