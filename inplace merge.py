def merge(arr, left, mid, right):
    mx = max(arr[mid], arr[right])+1

    i = left
    j = mid+1
    k = left

    while i <= mid and j <= right and k <= right:
        e1 = arr[i] % mx
        e2 = arr[j] % mx

        if (e1 <= e2):
            arr[k] += (e1*mx)
            i += 1
            k += 1
        else:
            arr[k] += (e2*mx)
            j += 1
            k += 1

    while i <= mid:
        e1 = arr[i] % mx
        arr[k] += (e1*mx)
        i += 1
        k += 1

    while j <= right:
        e1 = arr[j] % mx
        arr[k] += (e1*mx)
        j += 1
        k += 1

    for l in range(left, right+1):
        arr[l] //= mx


def check(arr, left, right):
    if left < right:
        mid = (left+right)//2
        check(arr, left, mid)
        check(arr, mid+1, right)
        merge(arr, left, mid, right)


arr = [2, 3, 1, 4]
n = len(arr)
check(arr, 0, n-1)
print(arr)
