
"""Create a function to compute sum of digits. Call this sum of digits
function to find the sum of digits of numbers ranges from 1001 to 22000"""

def sum_digits(number):
    number = str(number)
    sum =0
    for digit in number:
        sum = sum + int(digit)
    print(number, ' ',sum)

print('N    SUM')
for number in range(1001,22001):
    sum_digits(number)
