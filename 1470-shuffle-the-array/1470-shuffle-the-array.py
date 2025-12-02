class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=[]
        for i in range(len(nums)//2):
            n.append(nums[i])
            n.append(nums[i+(len(nums)//2)])
        return n
        