class Solution:
    def maxFreqSum(self, s: str) -> int:
        s1={'a','e','i','o','u'}
        v={}
        c={}
        for char in s:
            if char.lower() in s1:
                v[char.lower()]=s.count(char)
            else:
                c[char.lower()]=s.count(char)
        if len(v)>0:
            m=max(v.values())
        else:
            m=0
        if len(c)>0:
            m1=max(c.values())
        else:
            m1=0
        return m+m1
        
        