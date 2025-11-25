class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem=0
        if k%2==0 or k%5==0:
            return -1
        elif k==1:
            return 1
        else:
            for i in range(1,k+1):
                rem=(rem*10+1)%k
                if rem==0:
                    return i
