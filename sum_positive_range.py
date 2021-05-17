"""
Be Posi?ve! Create a func,on to sum up all posi,ve argument inputs. Inputs ranges from 0 to N,
where N can be any posi,ve number.
"""

def positive_sum(*numbers):
    return sum( [number for number in numbers if number>0])

print(positive_sum(-1,2,3,-4,5))

"""
OUTPUT:

10
"""