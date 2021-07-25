"""
Create a python recursive function to sum up all digits of the given number number until it becomes a
single digit number.
    1. Example : 208 => 2+0+8 => 10 => 1+0 = 1
    2. Example: 21 => 2+1 = 3
"""

def sum_of_digits(number):
    if number>10:
        sum=0
        for digit in str(number):
            sum+=int(digit)
        print(str(number)+"=>",end="")
        sum_of_digits(sum)
    else:
        print(str(number)+"=>"+str(1))    

        

sum_of_digits(208)
sum_of_digits(21)