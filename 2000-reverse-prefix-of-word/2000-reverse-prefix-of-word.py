class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        v=word.find(ch)
        if v!=-1:
            l=word[v::-1]+word[v+1::]
            return l
        else:
            return word
            
        