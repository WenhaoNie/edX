animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result=0
    for value in aDict.values():
        result += len(value)
    
    return result

print(how_many(animals))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest=0
    biggestkey=list(aDict.keys())[0]
    for key in aDict:
        if len(aDict[key])>biggest:
            biggest=len(aDict[key])
            biggestkey=key
    return biggestkey