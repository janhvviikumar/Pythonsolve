class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans=[]
        for elem in order:
            if elem in friends:
                ans.append(elem)
        return ans
        