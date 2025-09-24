class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        list1.append(i)
                        list1.append(j)
            if len(list1)>0:
                break;
        return list1;
            