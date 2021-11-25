def check(arr,n):
    profit =[0]*n

    max_profit = arr[n-1]
    for i in range(n-2,0,-1):
        if arr[i]>max_profit:
            max_profit=  arr[i]
        
        profit[i] = max(profit[i+1],max_profit-arr[i])

    print(profit)

    min_val = arr[0]
    for i in range(1,n):
        if arr[i]<min_val:
            min_val = arr[i]

        profit[i] = max(profit[i-1],profit[i]+(arr[i]-min_val))

    print(profit)
    
    result = profit[n-1]

    return result


arr = [10, 22, 5, 75, 65, 80]
k = len(arr)
print(check(arr,k))


Set min to location 0
Search the minimum element in the array
Swap it value at location min
Increment min position by 1.
Repeat above steps until array is sorted.

complexity:
o(n^2)