class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d={"type":0,"color":1,"name":2}
        count=0
        for i in range(len(items)):
            j=d[ruleKey]
            if items[i][j]==ruleValue:
                count+=1
        return count
        