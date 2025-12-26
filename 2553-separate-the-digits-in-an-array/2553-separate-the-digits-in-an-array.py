class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for elem in nums:
            b=list(str(elem))
            for n in b:
                ans.append(int(n))
        return ans

        