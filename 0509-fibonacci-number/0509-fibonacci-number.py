class Solution:
    def fib(self, n: int) -> int:
        answer=self.myfunc(n)
        return answer
    def myfunc(self,num):
        if num==0 or num==1:
            return num
        return self.myfunc(num-1)+self.myfunc(num-2)
        