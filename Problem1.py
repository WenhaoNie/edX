s = 'azcbobobegghakl'

#vowls = ['a','e','i','o','u','A','E','I','O','U']
vowls = 'aeiouAEIOU'
i = 0
for c in s:
    for v in vowls:
        if c == v:
            i = i+1

print('Number of vowls: {}'.format(i))


