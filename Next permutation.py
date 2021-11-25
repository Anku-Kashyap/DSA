def  check(nums,n):
        i = len(nums)-1
        while i>0:
            if nums[i-1]<nums[i]:
                break
            i = i-1
        i = i-1
        j = len(nums)-1
        while j>i:
            if nums[j]>nums[i]:
                break
            j=j-1
        nums[i],nums[j]=nums[j],nums[i]  
        nums[i+1:]=sorted(nums[i+1:])
        return nums

nums=  [2,3,1]
print(check(nums,len(nums)))