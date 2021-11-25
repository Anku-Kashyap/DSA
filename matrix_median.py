from  bisect import bisect_right as upper_bound

def check(arr,r,c):
    mi = arr[0][0]
    mx= 0
    for i in range(r):
        if arr[i][0]<mi:
            mi = arr[i][0]
        if arr[i][c-1]>mx:
            mx = arr[i][c-1]
        
    desired = (r*c+1)//2
    while mi<mx:
        mid=  mi+(mx-mi)//2
        place =[0];

        for i in range(r):
            j = upper_bound(arr[i],mid)
            place[0]= place[0]+j

            if place[0]<desired:
                mi =  mid+1
            else:
                mx=  mid
    return mi



    
        
        

M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

r,c = 3,3
print(check(M,r,c))