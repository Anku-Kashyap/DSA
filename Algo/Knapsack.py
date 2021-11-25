def final_cal(cap, res):
    i = 0 
    s = 0
    while cap>0:
        if cap>=res[i][1]:
            cap-=res[i][1]
            s += res[i][0]
            i+=1
        else:
            s += (res[i][0]*cap)//res[i][1]
            cap = 0
    return s

def cal_acc_profit(profit,w,cap):
    res = list(zip(profit,w))
    res.sort(reverse=True)
    return final_cal(cap, res)



def cal_acc_weight(profit,w,cap):
    res = list(zip(profit,w))
    res.sort(key = lambda x: x[1])
    return final_cal(cap,res)


def cal_acc_ratio(profit,w,cap):
    res =[0]*len(profit)
    for i in range(len(w)):
        res[i] = profit[i]//w[i]
    res = list(zip(profit,w,res))
    res.sort(key= lambda x: x[2],reverse=True)
    return final_cal(cap,res)

profit =[30,20,100,90,160]
w = [5,10,20,30,40]
cap = 60
print("When sorted accroding to profit: ",cal_acc_profit(profit,w,cap))
print("When sorted accroding to weight: ",cal_acc_weight(profit,w,cap))
print("When sorted optimally: ",cal_acc_ratio(profit,w,cap))

