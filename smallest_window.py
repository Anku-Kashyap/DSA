from collections import defaultdict
def check(a,n):
    if n<=1:
        return a
    
    dist_count = len(set(a))
    curr_count=  defaultdict(lambda:0)
    count,start =0,0
    min_len = n

    for j in range(n):
        curr_count[a[j]]+=1
    
        if curr_count[a[j]]==1:
            count+=1
        
        if count==dist_count:
            while curr_count[a[start]]>1:
                if curr_count[a[start]]>1:
                    curr_count[a[start]]-=1
                
                start+=1
            
            len_window = j-start+1

            if min_len>len_window:
                min_len = len_window
                start_index = start
    
    return str(a[start_index:start_index+min_len])

a = "GEEKSGEEKSFOR"
n = len(a)
print(check(a,n))