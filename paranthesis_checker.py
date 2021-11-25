def check(X):

    s = []
    for char in X:
        if char in ["{","(","["]:
            s.append(char)
        else:
            if not s:
                return False
            curr = s.pop()
            if curr == "{":
                if char!="}":
                    return False
            if curr =="(":
                if char!=")":
                    return False
            if curr=="[":
                if char!="]":
                    return False
            
    if s:
        return False
    return True

        




    

X  =["{","(","[","]",")"]
n = len(X)
print(check(X,n))