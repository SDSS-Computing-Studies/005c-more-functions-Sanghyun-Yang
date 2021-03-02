#!python3
"""
Create a function that determines the largest number in a list of values and returns it.
1 input parameter:
list: the numbers to be checked for the largest value

return: float value of the largest number

Sample assertions:
assert largest([3,10,3]) == 10
"""

def largest(lists):
    leng = len(lists)
    lists.sort()
    return lists[leng-1]
    pass

assert largest([3,10,3]) == 10