class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig=[]
        s=""
        for elem in digits:
            s=s+str(elem)
        num=int(s)+1
        temp=list(str(num))
        for elem in temp:
            dig.append(int(elem))
        return dig;