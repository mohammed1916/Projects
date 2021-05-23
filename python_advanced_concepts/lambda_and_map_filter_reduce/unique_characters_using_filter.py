"""
Write a function called is_unique. This function should take a string and should check
whether all characters of the string is unique/not. Example: If the input string is
“abcd”, all characters are unique, hence it should return True. Another example, if the
string is “abaa”, then this function should return False.
1. Create a List L of size 10 with random strings of length > 1.
2. Write a python snippet to check is_unique nature for all elements of L. (Hint:
Use map function)
3. Apply filter function, to get only unique elements from L.
"""
import random
import string

#List L of size 10 with random strings of length > 1
L = [''.join(random.choice(string.ascii_letters) for i in range(random.randrange(2,10))) for _ in range(10) ]

#sample list for debug, uncomment it for testing
# L = ['abaa','abcd']
print(L)

#lambda function for filter
is_unique = lambda s: len(list(set(s))) == len(s)


print(list(filter(is_unique,L)))