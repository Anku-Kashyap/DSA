def total_profit(profit,job):
    m = max(job)
    li =[i+1 for i in range(m)]
    total = 0
    arr = sorted(list(zip(profit,job)),reverse=True)
    for i in range(len(profit)):
        a = arr[i][1]
        for j in range(len(li)):
            if li[j]<=a and li[j]!=0:
                total+=arr[i][0]
                li[j] = 0
                break
    return total


profit = [20,15,10,5,1]
job =[2,2,1,3,3]
print("Total Profit: ",total_profit(profit,job))