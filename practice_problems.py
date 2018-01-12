"""Coding practice problems"""

from collections import defaultdict

def count_appearances(elements):
    '''
    This is a function adding 1 to each element 
    '''
    element_counts_map = defaultdict(int)
    for element in elements:
        element_counts_map[element] = element_counts_map.get(element, 0) + 1
    return element_counts_map
