class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(image)):
            temp=image[i][::-1]
            t=[]
            for j in range(len(image[i])):
                if temp[j]==1:
                    t.append(0)
                else:
                    t.append(1)
            ans.append(t)
        return ans
                


        