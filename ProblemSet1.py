s = 'azcbobobegghakl'
#s = 'obooobobbrbob'
#Problem 1

#vowls = ['a','e','i','o','u','A','E','I','O','U']
vowls = 'aeiouAEIOU'
i = 0
for c in s:
    for v in vowls:
        if c == v:
            i = i+1

print('Number of vowls: {}'.format(i))



#Problem 2
target = 'bob'
i = 0
for j in range(len(s)-len(target)+1):
    if target == s[j:j+len(target)]:
        i += 1

print('Number of times {} occurs is: {}'.format(target,i))



#Problem 3
current=""
longest=s[0]
currentl=0
longestl=1
for j in range(len(s)-1):
    if s[j+1] >= s[j]:
        if currentl == 0:
            currentl = 2
            current = s[j]+s[j+1]
        else:
            currentl += 1
            current += s[j+1]

        if currentl > longestl:
            longestl = currentl
            longest = current
    else:
        current = ""
        currentl = 0

print('Longest substring in alphabetical order is: {}'.format(longest))
