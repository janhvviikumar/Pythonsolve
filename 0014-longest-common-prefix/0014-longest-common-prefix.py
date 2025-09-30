class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        s=""     
        for j in range(len(strs[0])):
            count=0
            found=0
            for i in range(len(strs)):
                if len(strs)==1:
                    s=s+strs[i][j]
            for i in range(1,len(strs)):
                if strs[0][j]==strs[i][j]:
                    count+=1
                    if count==(len(strs)-1):
                        s=s+strs[0][j]
                else:
                    found=1
                    break
            if found==1:
                break

                
            
        return s;
        
