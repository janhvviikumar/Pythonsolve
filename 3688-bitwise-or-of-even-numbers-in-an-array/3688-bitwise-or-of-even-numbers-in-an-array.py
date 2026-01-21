class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        temp=0
        for elem in nums:
            if elem%2==0:
                temp=elem|temp
        return temp
        
        
        