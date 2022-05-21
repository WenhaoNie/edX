import sys
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    nTrials = 10000
    sDiff = sys.maxsize
    results = None
    rTotal = sys.maxsize
    while nTrials>0:
        result = np.random.randint(0,2,len(choices))
        diff = total - sum(result*choices)
        if diff > 0 and diff < sDiff:
            results = result
            sDiff = diff
        elif diff == 0:
            if rTotal>sum(result):
                rTotal = sum(result)
                results = result
            sDiff = diff
        nTrials -= 1
    return results


