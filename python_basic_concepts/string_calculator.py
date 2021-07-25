"""String Calculator - Implement String calculator with following functions.
• Function that reverses the given string S. (A)
• Function that returns total A’s available (it can be ‘a’ or ‘A’) int given
string S. (B)
• Function that takes 2 inputs string S and index and returns element at
given index. If the index is not available, it should return 0 as the
output. (C)
• Function that multiples given string 5 times (D)
- Implement all the above functions.
- Get input and pass it to the reverse function, get the output from it and call
function C, function C takes 2 params, first param should be output from function
A and second param should be output from function B. Get the output. If the
output is not 0, call function D and print output. Else call print “Completed without
multiply” as the output.
Sample I/O:
Input: “Hari”
Output:
- Reverse of Hari => iraH
- Output from function C => C(“iraH”, 1) => r
- Final output = 5 times of r = rrrrr."""

def A(string):
    return string[::-1]

def B(string):
    letters=['A','a']
    count=0
    for letter in string:
        if letter in letters:
           count+=1 
    return count

def C(string,index):
    #As index will always be positive number as it represents count of A,a
    #Therefore no comparison to check for negative idex is needed
    return ( 0 , string[index] )[index<len(string)]   

def D(string):
    return string*5

input=str(input('Enter Input: '))
output_C = C( A(input) , B(input) )
if output_C != 0:
    print( D(output_C) )
else:
    print('Completed without multiply')