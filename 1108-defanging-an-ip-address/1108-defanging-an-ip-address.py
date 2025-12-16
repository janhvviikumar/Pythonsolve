class Solution:
    def defangIPaddr(self, address: str) -> str:
        for char in address:
            if char==".":
                a=address.replace(".","[.]")
        return a
        