class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum=0
        digit=0
        for elem in nums:
            sum+=elem
            l=list(str(elem))
            for dig in l:
                digit+=int(dig)
        return abs(sum-digit)
        