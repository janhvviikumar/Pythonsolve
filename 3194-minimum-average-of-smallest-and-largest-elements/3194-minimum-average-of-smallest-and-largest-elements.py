class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        i=0
        averages=[]

        for i in range(len(nums)//2):
            o=(max(nums)+min(nums))/2
            averages.append(o)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(averages)

        