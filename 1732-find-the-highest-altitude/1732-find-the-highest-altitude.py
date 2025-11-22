class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        diff=0
        l=[0]
        for i in range(len(gain)):
            diff+=gain[i]
            l.append(diff)
        return max(l)
        