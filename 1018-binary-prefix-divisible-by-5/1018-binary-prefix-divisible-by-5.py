class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        l=[]
        final=[]
        st=nums[0]
        l.append(st)
        for i in range(1,len(nums)):
            n=st*2+nums[i]
            l.append(n)
            st=n
        for elem in l:
            if elem%5==0:
                final.append(True)
            else:
                final.append(False)
        return final
                
                