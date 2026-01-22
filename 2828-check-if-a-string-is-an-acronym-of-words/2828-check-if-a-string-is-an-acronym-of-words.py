class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n=""
        for word in words:
            n+=word[0]
        return True if n==s else False

        