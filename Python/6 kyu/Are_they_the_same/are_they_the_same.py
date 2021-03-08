# Description:
# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) 
# that checks whether the two arrays have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

import math
def comp(a,b):
    return a==b if a is None or b is None else sorted([i**2 for i in a])==sorted(b)