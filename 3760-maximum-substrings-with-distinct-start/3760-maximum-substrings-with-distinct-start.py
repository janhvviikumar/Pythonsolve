class Solution:
    def maxDistinct(self, s: str) -> int:
        s1=set(s)
        return len(s1)
        