#Problem 3
from re import I


def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    chosen = []
    avaSize = max_size
    try:
        if songs[0][2]>avaSize:
            return chosen
        else:
            chosen.append(songs[0][0])
            avaSize -= songs[0][2]
    except IndexError:
        return chosen

    try:
        sortedSongs = songs[1:]
        sortedSongs.sort(key = lambda x:x[2])
        counter = 0
        while(avaSize>=0):
            if sortedSongs[counter][2]<=avaSize:
                chosen.append(sortedSongs[counter][0])
                avaSize -= sortedSongs[counter][2]
                counter += 1
            else:
                break
    except IndexError:
        return chosen
    
    return chosen

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
#songs = [('Roar',4.4, 11.1)]
#songs = []
max_size = 11
print(song_playlist(songs, max_size))

#Problem 4
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    memo = {}
    value = max_helper(L, memo)
    sortedMemo  = sorted(memo.items(), key = lambda item:item[1])
    try:
        return sortedMemo.pop()[1]
    except IndexError:
        return 0

def max_helper(L, memo):
    if L == []: return 0 
    try:
        return memo[tuple(L)]
    except KeyError:
        result = int((max_helper(L[1:], memo) + L[0] +\
                max_helper(L[:-1], memo) + L[-1])/2)
        memo[tuple(L)] = result
        return result

list1 = [3, 4, -1, 5, -4]
print(max_contig_sum(list1))
list2 = [3, 4, -8, 15, -1, 2]
print(max_contig_sum(list2))
list3 = [2,2,2,2,0]
print(max_contig_sum(list3))
list4 = []
print(max_contig_sum(list4))
list5 = [-2, -3, -5]
print(max_contig_sum(list5))
list6 = [-7, -3, -5]
print(max_contig_sum(list6))

#Problem 7

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    i = 0
    
    while (test(i) == False and test(i*(-1)) == False):
        i += 1
    if test(i) == True:    return i
    else: return i*(-1)


#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))