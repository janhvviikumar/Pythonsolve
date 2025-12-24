class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set(allowed)
        count=0
        for elem in words:
            temp=set(elem)
            for ch in temp:
                if ch not in s:
                    count+=1
                    break
        return (len(words)-count)
        
        