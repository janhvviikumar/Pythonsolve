class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for elem in nums:
            if (len(str(elem))%2)==0:
                count+=1
        return count
        