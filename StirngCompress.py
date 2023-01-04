from genericpath import exists
from itertools import count


def stringcompress(s):
    new_s=""
    n=len(s)
    count=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            new_s=new_s+s[i]+str(count)
            count=1
            
    return new_s+s[n-1]+str(count)
            
            

s="aaabccdee"
print(stringcompress(s))