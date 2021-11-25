def lps( s):
		# code here
		n = len(s)
		lp =[0]*n
		l =0
		i=1
		while i<n:
		    if s[i]==s[l]:
		        l+=1
		        lp[i] = l
		        i+=1
		    else:
		        if l!=0:
		            l = lp[l-1]
		        else:
		            lp[i] = 0
		            i+=1
		            
	    res = lp[n-1]
		return res

        