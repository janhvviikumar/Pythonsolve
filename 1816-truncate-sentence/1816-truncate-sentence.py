class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=s.split(" ")
        l=l[:k:]
        s=" ".join(l)
        return s

        
        