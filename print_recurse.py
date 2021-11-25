R= 3
C = 3
def printutil(arr,m,n,output):
    
    output[m] = arr[m][n]

    if m==R-1:
        for i in range(R):
            print(output[i],end=" ")
        print("\n")
        return 
    

    for i in range(C):
        if arr[m+1][i]!="":
            printutil(arr,m+1,i,output)


def check(a):
    output = [""]*R
    for i in range(C):
        if a[0][i]!="":
            printutil(a,0,i,output)
    



a = [["you", "we",""],
        ["have", "are",""],
        ["sleep", "eat", "drink"]]
print(check(a))