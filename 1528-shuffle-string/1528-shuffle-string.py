class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        op=[]
        for i in range(len(indices)):
            temp=indices.index(i)
            op.insert(i,s[temp])
        a="".join(op)
        return a
                