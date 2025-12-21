class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        op=set()
        for i in range(len(words)):
            w=""
            for j in range(len(words[i])):
                t=ord(words[i][j])-97
                w+=l[t]
            op.add(w)
        return len(op)


        