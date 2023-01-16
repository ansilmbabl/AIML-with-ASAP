"""
Use of filter in lambda
filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

syntax:
filter(function, sequence)

Parameters:
function: function that tests if each element of a sequence true or not.
sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.

Returns:
returns an iterator that is already filtered.
"""

l = [12,45,23,90,34,89,100]
newlist = list(filter(lambda x:x%3==0,l))
newlist
