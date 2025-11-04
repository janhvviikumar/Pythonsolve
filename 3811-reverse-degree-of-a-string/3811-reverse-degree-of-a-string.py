class Solution:
    def reverseDegree(self, s: str) -> int:
        l=['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
        count=0
        for ch in range(len(s)):
            for i in range(len(l)):
                if s[ch]==l[i]:
                    count+=(ch+1)*(i+1)
                    break
        return count