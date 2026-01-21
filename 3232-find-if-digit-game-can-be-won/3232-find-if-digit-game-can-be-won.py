class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        nums.sort()
        single=0
        doubl=0
        for elem in nums:
            if len(str(elem))==1:
                single+=elem
            else:
                doubl+=elem
        
        return True if doubl!=single else False

        