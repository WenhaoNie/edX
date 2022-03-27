from pyrsistent import v


def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    tri = 1
    i = tri + 1
    isTri = False
    while tri <= k:
        if tri == k: isTri = True 
        tri += i
        i += 1
    
    return isTri


def primes_list(N):
    '''
    N: an integer
    '''
    # Your code here
    if N <= 2:
        return [2]
    else:
        primesLast = primes_list(N-1)
        div = False
        for p in primesLast:
            if N%p == 0: 
                div = True
                break
        if not div: 
            primesLast.append(N)
        
        return primesLast


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    valueKeyCount = {}
    # valueKeyCount maps aDict's value to key
    # also count how many times it appears in aDict
    # valueKeyCount -> value:(key, count)
    for key, value in aDict.items():
        if value not in valueKeyCount:
            valueKeyCount[value] = (key,1)
        else:
            temp_key, temp_count = valueKeyCount[value]
            valueKeyCount[value] = (temp_key, temp_count+1)
    
    # then iterate valueKeyCount to find the values that 
    # appear exactly once, then put the keys in a list

    uniqueList = []
    for key, value in valueKeyCount.items():
        if value[1] == 1:
            uniqueList.append(value[0])

    uniqueList.sort()

    return uniqueList

print(uniqueValues({10: 1, 8: 2, 7: 0, 6: 0, 2: 4, 1: 0}))
print(uniqueValues({1: 1, 2: 1, 3: 1}))
print(uniqueValues({}))
print(uniqueValues({1:1,2:1,3:0,4:0,5:2}))