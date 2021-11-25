def check(nums,n,target):
    
    low=  0
    high = n-1
    while low<=high:
        mid=  (low+high)//2
        if nums[mid]==target:
            return mid
        elif target<nums[low] and target>nums[high]:
            return -1
        
        elif nums[low]<=nums[mid]:
            if nums[low]<=target<=nums[mid]:
                high = mid-1
            else:
                low = mid+1

        else:
            if nums[mid]<=target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    return -1




nums = [4,5,6,7,0,1,2]
k = 13
n = len(nums)
print(check(nums,n,k))