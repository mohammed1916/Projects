"""
Star Genera?on: Create a python func,on which takes a number N and generates following star
pacern accordingly. N ranges from 1 to any posi,ve number. Make sure if N is not passed as
argument while calling func,on, it should take 3 as it’s default value.
Example: N = 4
Output:
*
@@
***
@@@@
Example: N = 2
*
@@
"""

def star_genetator(no_of_rows = 3):
    #iterrate through each row printing the charater pattern in alternate fashion
    for times in range(int(no_of_rows)+1):
        if times %2 != 0:
            print_pattern('*',times)
        else:
            print_pattern('@',times)

def print_pattern(char,multiplier):
    print(char*multiplier)


input_from_user = input( "Enter number for pattern: ")
#if no input is given from the user
if input_from_user == '':
    star_genetator()
else:
    star_genetator(input_from_user)