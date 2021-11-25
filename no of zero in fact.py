def isvalid(arr,m,mid):
    studentsRequired = 1
    curr_sum = 0
 
    # iterate over all books
    for i in range(n):
 
        # check if current number of pages are
        # greater than curr_min that means
        # we will get the result after
        # mid no. of pages
        if (arr[i] > mid):
            return False
 
        # count how many students are required
        # to distribute curr_min pages
        if (curr_sum + arr[i] > mid):
 
            # increment student count
            studentsRequired += 1
 
            # update curr_sum
            curr_sum = arr[i]
 
            # if students required becomes greater
            # than given no. of students, return False
            if (studentsRequired > m):
                return False
 
        # else update curr_sum
        else:
            curr_sum += arr[i]
 
    return True

def check(arr,n,m):
    if n<m:
        return -1
    arr.sort()
    low= max(arr)
    high = sum(arr)
    while low<=high:
        mid =  (low+high)//2
        if isvalid(arr,m,mid):
            res = mid
            high = mid-1
        else:
            low = mid+1

    return 

arr=  [51 ,151 ,227 ,163 ,55]
n = len(arr)
m = 3
print(check(arr,n,m))