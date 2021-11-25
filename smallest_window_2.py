max_chars =  256
def check(string,pat):
    n = len(string)
    m = len(pat)
    if n<m:
        return False

    hash_str = [0]*max_chars
    hash_pat  =[0]*max_chars

    for i in range(m):
        hash_pat[ord(pat[i])]+=1

    start,start_index,min_len = 0,-1,float('inf')

    count= 0

    for j in range(n):
        hash_str[ord(string[j])]+=1

        if hash_str[ord(string[j])]<=hash_pat[ord(string[j])]:
            count+=1
        
        if count==m:

            while hash_str[ord(string[start])]>hash_pat[ord(string[start])] or hash_pat[ord(string[start])]==0:

                if hash_str[ord(string[start])]>hash_pat[ord(string[start])]:
                    hash_str[ord(string[start])]-=1
                start+=1
            
            len_window = j-start+1
            if min_len>len_window:
                min_len = len_window
                start_index = start
    
    if start_index==-1:
        return False
    
    return string[start_index:start_index+min_len]


string = "this is a test string"
pat = "tist"
print(check(string,pat))