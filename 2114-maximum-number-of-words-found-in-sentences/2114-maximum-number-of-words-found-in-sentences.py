class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        temp=0
        for elem in sentences:
            l=elem.split()
            temp=len(l)
            if temp>ans:
                ans=temp
        return ans
            

            
        