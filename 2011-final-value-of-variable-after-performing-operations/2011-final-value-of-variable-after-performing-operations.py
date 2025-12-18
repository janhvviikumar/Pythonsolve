class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d={"--X":-1,"X++":1,"++X":1,"X--":-1}
        val=0
        for elem in operations:
            for v in d.keys():
                if elem in v:
                    val+=d[v]
        return val

        