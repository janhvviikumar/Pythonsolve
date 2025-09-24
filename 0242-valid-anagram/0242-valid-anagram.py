class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        a.sort()
        b=list(t)
        b.sort()
        count=0
        if len(a)==len(b):
            for i in range(len(a)):
                if a[i]==b[i]:
                    count+=1
        if count==len(a):
            return True
        return False