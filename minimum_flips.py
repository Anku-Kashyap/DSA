def getmin(s,expected):
    flip=0
    for i in range(len(s)):
        if s[i]!=expected:
            flip+=1
        expected = '1' if (expected == '0') else '0'
    return flip

def check(s):
    return min(getmin(s,'0'),getmin(s,'1'))
    
S = "001"
n = len(S)
print(check(S))