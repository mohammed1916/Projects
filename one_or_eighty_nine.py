"""1 or 89 applica,on.
Mr.Talentpy would like to create a func,on one_or_eight which takes an integer input (no) and
performs following opera,on.
1. Square the number if it is single digit. (Eg: 3, then 3 * 3 = 9)
2. If it is not single digit, square each digits and add. (Eg: 12, then (1*1) + (2*2) = 1+4 = 5
You have to repeat step (1) and (2) un,l you reach 1 or 89. Note that, always your result will reach
1 or 89 for sure. Input must be a posi,ve number.
If the opera,on reaches at the end, 89 return True, if opera,on reaches 1 at the end return False.

Sample Input/Output: 1
• Input: 3
• Output : 3 *3 = 9 => 9 * 9 => 81 => (64+1) = 65 => (36+25) = 61 => (36+1) => 37 = (9+49) => 58
=> (25+64) => 89.
• Explana,on : True

Sample Input/Output: 2
• Input: 10
• Output : 1 square + 0 square = 1+0 = 1
• Explana,on : False"""


def one_or_eight(number):
    #Optional line for debug
    #print( number ,"->" ,end =" ")
    if number == 89:
        return True
    elif number == 1:
        return False

    number = str(number)

    if len(number) == 1:
        return one_or_eight( pow (int(number),2) )
    else:
        total = 0
        total = sum([pow(int(digit),2) for digit in number ])
        return one_or_eight( total )

num = int(input("Enter number:"))
result = one_or_eight(num)
print( result )