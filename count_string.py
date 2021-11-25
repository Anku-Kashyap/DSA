def check(ii,needle,row,col,hay,row_max,col_max):

    found = 0
    if (row>=0 and row<=row_max and col>=0 and col<=col_max and needle[ii]==hay[row][col]):
        match = needle[ii]
        ii+=1
        hay[row][col] = 0
        if ii==len(needle):
            found=1
        else:
            found+=check(ii,needle,row,col+1,hay,row_max,col_max)
            found+=check(ii,needle,row,col-1,hay,row_max,col_max)
            found+=check(ii,needle,row+1,col,hay,row_max,col_max)
            found+=check(ii,needle,row-1,col,hay,row_max,col_max)
   
        hay[row][col] = match
    return found

def searchString(needle, row, col,strr,
                row_count, col_count):
    found = 0
    for r in range(row_count):
        for c in range(col_count):
            found += check(0, needle, r, c,
                        strr, row_count - 1, col_count - 1)
             
    return found

arr = [["D", "D", "D", "G", "D", "D"],
       ["B", "B", "D", "E", "B", "S"],
       ["B", "S", "K", "E", "B", "K"],
       ["D", "D", "D", "K", "D", "E"],
       ["D", "D", "D", "S", "D", "E"],
       ["D", "D", "D", "D", "D", "G"]]
s = "GEEKS"
n = len(arr)
m = len(arr[0])

print(searchString(s,0,0 ,arr,n,m))
