class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        count=0
        for elem in words:
            if elem==elem[::-1]:
                count+=1
                return elem
                break
        if count==0:
            return ""
        