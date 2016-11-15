#!/usr/bin/env python

"""
First, you are to create a BinarySearch class, that inherits from the list class the following:
the __init__() takes two integers as parameters, a and b.
a is the length of the list to be created and b is the step or difference between consecutive values.
It should also initialize an instance variablelength`, that returns the number of elements in the array

Once you are done, create another method called search, it will take just one argument 
which is the value you are to find.
The search function should return a dictionary object, which contains
count, the number of times you function iterated to find the index of the number in question index,
 the index of the number in question

The search method should implement the binary search algorithm, each time you iterate, 
you should increase the count, to test how efficient your implementation is.
"""
class BinarySearch(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.alist = range(b, (a * b) + 1, b)  # generate list here
        self.length = a

    def __getitem__(self, item):
        return self.alist[item]

    def __setitem__(self, item, value):
        return self.alist[item] == value

    def search(self, value):
        """
        Find if the value is in the list
        """
        first_element = 0
        last_element = self.a - 1
        count = 0
        # check if value is equals first or last element
        if self.alist[first_element] == value:
            return {'count': 0, 'index': first_element}
        if self.alist[last_element] == value:
            return {'count': 0, 'index': last_element}
        # else loop through the list while updating the count
        while first_element <= last_element:
            mid_point = (first_element + last_element) // 2
            count += 1
            if self.alist[mid_point] == value:
                return {'count': count, 'index': mid_point}
            elif value > self.alist[mid_point]:
                first_element = mid_point + 1
            elif value < self.alist[mid_point]:
                last_element = mid_point - 1
        # for value > last item. value out of range
        if first_element > last_element:
            return {'count': 0, 'index': -1}
