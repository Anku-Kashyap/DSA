def check(words,n):
    s = words.copy()
    l  = list(zip(words,s))
    for i in range(n):
        l[i][0] = ''.join(sorted(l[i][0]))
    return l

words =['act','god','dog','tac','cat']
n = len(words)
print(check(words,n))