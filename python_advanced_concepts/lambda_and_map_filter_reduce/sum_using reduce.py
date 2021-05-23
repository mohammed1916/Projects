#Write python script to add elements of list L using reduce() function

import functools

l = [1,2,3,4,5]

sum_elements = lambda x,y : x+y

final_sum = functools.reduce(sum_elements,l)

print(final_sum)

"""
Output:
---------
15
"""