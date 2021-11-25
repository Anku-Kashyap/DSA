def is_valid(ip):
    ip = ip.split(".")

    for i in ip:
        if len(i)>3 or int(i)<0 or int(i) >255:
            return False
        
        if len(i) >1 and int(i) ==0:
            return False
        
        if len(i)>1 and int(i)!=0 and i[0]=='0':
            return False
    return True

def convert(a):
    n = len(a)
    if n>12:
        return False
    snew = a
    l = []
    for i in range(1,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]

                if is_valid(snew):
                    l.append(snew)
                
                snew = a
    return l


a = "25525511135"
print(convert(a))