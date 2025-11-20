class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l3=[]
        for i in range(len(nums1)):
            temp=-inf
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    temp=nums1[i]
                if (temp!=-inf) & (temp<nums2[j]):
                    l3.append(nums2[j])
                    break
                elif (temp>=nums2[j]) and (j==(len(nums2)-1)):
                    l3.append(-1)
        return l3