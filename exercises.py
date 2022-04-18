# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 3 == 1:
                bag1.append(items[j])
            elif (i >> j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)