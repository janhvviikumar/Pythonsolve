class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(' : ')', '[' : ']', '{' : '}',}
        curr_op = []
        for x in s:
            if x in brackets:
                curr_op.append(x)
            elif not curr_op:
                return False
            else:               
                t = curr_op.pop(-1)
                if brackets[t] != x:
                    return False
            
        return not curr_op