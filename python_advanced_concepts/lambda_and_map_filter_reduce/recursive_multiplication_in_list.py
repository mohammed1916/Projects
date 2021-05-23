#Write python recursive function to perform multiplication of all elements of list L.

import functools

L = [1,2,3,4,5]

#lambda to be used in reduce
multiply = lambda x,y : x*y

multiplication_of_list_elements = functools.reduce(multiply, L)
print(multiplication_of_list_elements)