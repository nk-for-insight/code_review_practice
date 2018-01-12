"""Coding practice problems"""

def count_appearances(elements):
'''Counts appearances in elements'''
    element_counts_map = {}
    for element in elements:
        element_counts_map[element] = element_counts_map.get(element, 0) + 1
    return element_counts_map
