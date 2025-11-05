class Solution:
    def reverseDegree(self, s: str) -> int:
        count=0
        for ch in range(len(s)):
            count+=(ch+1)*((ord('z')-ord(s[ch]))+1)
        return count