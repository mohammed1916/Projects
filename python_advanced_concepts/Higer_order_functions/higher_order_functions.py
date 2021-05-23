"""
Create three functions as follows -
1. def remove_vowels(string) - which will remove all vowels from the given
string. For example if the string given is “aeiru”, then the return value should
be ‘r’
2. def remove_consonants(string) - which will remove all consonants from
given string. For example, if the string given is “aeri”, then the return value
should be ‘aei’.
3. def caller -> This function should 2 parameters
1. Function to call
2. String argument
This caller function should call the function passed as a parameter, by
passing second parameter as the input for the function. Example: caller(remove_vowles,
“aeiru”) should call remove_vowels function and should return ‘r’ as the output.
"""
def remove_vowels(string):
    vowels = ['a','e','i','o','u']
    return ''.join(map (str, [character for character in string if character in vowels]) )

def remove_consonants(string):
    vowels = ['a','e','i','o','u']
    return ''.join(map (str, [character for character in string if character not in vowels]) )

def caller(func , string):
    return func(string)

print(caller(remove_vowels,"aeiru"))
print(caller(remove_consonants,"aeir"))