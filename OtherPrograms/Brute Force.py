# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:50:33 2018

@author: pl89155
"""

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        combo = []
        combo1 = []
        for j in range(N):
            # test bit jth of integer i
            if (i//3**j) % 3 == 2:
                combo.append(items[j])
            elif (i//3**j) % 3 == 1:
                combo1.append(items[j])
        yield (combo, combo1)
        
test = [1,2,3,4,5,6]

print(list(yieldAllCombos(test)))