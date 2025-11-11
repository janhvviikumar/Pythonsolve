class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num1=[]
        n=set(nums)
        for i in range(1,len(nums)+1):
            if i not in n:
                num1.append(i)
            i+=1
        return num1