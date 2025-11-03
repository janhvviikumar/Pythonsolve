class Solution:
    def reverseVowels(self, s: str) -> str:
        s1={"A","a","E","e","I","i","O","o","U","u"}
        s2=list(s)
        l,r=0,len(s)-1
        while l<r:
            if s2[l] in s1 and s2[r] in s1:
                s2[l],s2[r]=s2[r],s2[l]
                l+=1
                r+=-1
            elif s2[l] not in s1:
                l+=1
            elif s2[r] not in s1:
                r+=-1
        return "".join(s2)
        