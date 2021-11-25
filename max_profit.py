def max_profit(arr,n):
    minvalue = arr[0]
    profit = 0
    for i in range(n):
        if arr[i]<minvalue:
            minvalue = arr[i]
        else:
            profit  = max(profit,arr[i]-minvalue)
    return profit
arr  =[7,1,2,3,5,4,15,17,9,20]
n = len(arr)
print(max_profit(arr,n))