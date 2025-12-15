class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        f=""
        for elem in l:
            f+=elem[::-1]+" "
        return f[:len(f)-1:]
                