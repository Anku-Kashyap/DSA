def check(List,k):
    n = len(List)
    m = len(List[0])
    left,right=  0,m*n-1

    while left<=right:
        piv=  (left+right)//2
        x,y = piv//n,piv%n
        if List[x][y]==k:
            return True
        elif List[x][y]<k:
            left = piv+1
        else:
            right= piv-1
    return False

List=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 5
print(check(List,target))