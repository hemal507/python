def isOneSwapEnough(s):
        if len(s) == len(set(s)) :
                return False
        if s == s[::-1] :
                return True
        else :
                for i in range(len(s)) :
                        for j in range(len(s)) :
   	                     t = list(s)
                             t[i],t[j] = t[j],t[i]
                             if t == t[::-1] :
                  	           return True
        return False

