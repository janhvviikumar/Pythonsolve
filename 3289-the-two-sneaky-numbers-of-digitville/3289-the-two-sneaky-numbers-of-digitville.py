class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        op=[]
        for elem in nums:
            if nums.count(elem)==2:
                op.append(elem)
        op.sort()
        op.pop(1)
        op.pop(2)
        return op

        