class Solution:
    def isPalindrome(self, x: int) -> bool:
        count=0
        if x>0 or x==0:
            l=list(map(int,str(x)))
            for i in range(len(l)//2):
                if l[i]==l[(len(l)-1)-i]:
                    count+=1
            if count==(len(l)//2)+1 or count==len(l)//2:
                return True;
    
        return False;

