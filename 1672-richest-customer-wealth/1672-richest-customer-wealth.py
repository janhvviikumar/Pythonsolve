class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for i in range(len(accounts)):
            count=0
            for j in range(len(accounts[i])):
                count+=accounts[i][j]
            l.append(count)
        return max(l)
        