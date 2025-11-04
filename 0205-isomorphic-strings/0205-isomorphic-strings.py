class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ls=[]
        lt=[]
        for char in s:
            ls.append(s.find(char))
        for char in t:
            lt.append(t.find(char))
        if ls==lt:
            return True
        else:
            return False