def check(a,b):
    if len(a)==0 and len(b)==0:
        return True
    
    if len(a)>1 and a[0]=='*' and len(b)==0:
        return False
    
    if (len(a)>1 and a[0]=='?') or (len(a)!=0 and len(b)!=0 and a[0] ==b[0]):
        return check(a[1:],b[1:])

    if len(a)!=0 and a[0]=='*':
        return check(a[1:],b) or check(a,b[1:])
    
    return False



wild  = "ge*ks"
pat = "geeks"
print(check(wild,pat))