class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l=[]
        for elem in arr:
            if arr.count(elem)==1:
                l.append(elem)
        if len(l)<k:
            return ""
        else:
            return l[k-1]
                