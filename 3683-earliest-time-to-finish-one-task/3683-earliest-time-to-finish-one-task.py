class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        l=[]
        for i in range(len(tasks)):
            sum=0
            for j in range(len(tasks[i])):
                sum+=tasks[i][j]
            l.append(sum)
        return min(l)
        