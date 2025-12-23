class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1=set(s)
        ins=[]
        sum=0
        for char in s1:
            if s.count(char) > t.count(char):
                ins.append(s.count(char) - t.count(char))
        for elem in ins:
            sum+=elem
        return sum
        
                