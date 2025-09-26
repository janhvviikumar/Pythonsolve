class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s=s.replace("IV","IIII").replace("IX","VIIII").replace("XL", "XXXX"). replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        count=0
        for i in range(len(s)):
            for key in d.keys():
                if s[i]==key:
                    count+=d[key]
        return count;