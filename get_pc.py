def check(n,seq):
    seq = list(seq)
    arr =[0]*n
    aux = []
    for i in range(len(seq)):
        if seq[i] in arr:
            a = arr.index(seq[i])
            arr[a]=0
        elif 0 in arr:
            for j in range(n):
                if arr[j]==0:
                    arr[j]= seq[i]
                    break
        else:
            if seq[i] not in aux:
                aux.append(seq[i])
    return len(aux)

n = 1
seq = "ABCBCADEED"
print(check(n,seq))