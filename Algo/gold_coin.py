def check_faulty(a):
    s =  -1
    for i in range(len(a)):
        if a[i]!=10:
            s = i+1
            return s


a = [10,10,10,10,10,10,11,10,10,10]
print(f"Machine no {check_faulty(a)} faulty.")

b = [10,10,10,9,10,10,10,10,10,10]
print(f"Machine no {check_faulty(b)} faulty.")