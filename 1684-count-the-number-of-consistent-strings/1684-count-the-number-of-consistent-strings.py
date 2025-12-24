class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=list(allowed)
        count=0
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in s:
                    count+=1
                    break
        return (len(words)-count)
                
                