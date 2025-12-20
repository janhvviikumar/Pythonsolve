class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])):
            l=[]
            l1=[]
            for j in range(len(strs)):
                l.append(strs[j][i])
                l1.append(strs[j][i])
            l1.sort()
            if l1!=l:
                count+=1
        return count
            
        