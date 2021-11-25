from itertools import permutations

words = [''.join(p) for p in permutations('prog')]

#print(words)

"""def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
        print(words)
        get_permutation(words, i + 1)

"""

def per(a,l,r):
    if l==r:
        print(''.join(a),end=" ")
        return
    
    for i in range(l,r+1):
        a[l],a[i] = a[i],a[l]
        per(a,l+1,r)
        a[l],a[i] = a[i],a[l]


s =list("ABC")
print(per(s,0,2))