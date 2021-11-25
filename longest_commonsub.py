strs = ["dog","racecar","car"]
strs.sort()
for i in range(len(strs[0])):
    if strs[0][i]!=strs[-1][i]:
        return strs[0][:i]
return strs[0]
