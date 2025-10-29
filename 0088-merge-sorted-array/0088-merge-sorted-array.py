class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''nums1=nums1+nums2
        i=0
        while i<len(nums1):
            if nums1[i]==0:
                nums1.remove(nums1[i])
            else:
                i+=1
        nums1.sort()'''
        nums1[m:] = nums2
        nums1.sort()
        
        

        