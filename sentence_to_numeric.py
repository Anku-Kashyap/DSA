def check(arr,str):
    n = len(arr)
    res =""
    for i in range(n):
        if arr[i]==" ":
            res+="0"
        else:
            position = ord(arr[i])-ord('A')
            res+=str[position]
    return res


arr  = "ALGORITHM"
str = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999" ]
print(check(arr,str))