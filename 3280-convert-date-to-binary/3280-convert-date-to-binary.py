class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l=date.split("-")
        n=[]
        for elem in l:
            e=bin(int(elem))[2:]
            n.append(e)
        o="-".join(n)
        return o

        