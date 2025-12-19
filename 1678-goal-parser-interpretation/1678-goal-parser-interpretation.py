class Solution:
    def interpret(self, command: str) -> str:
        d={'G':'G',"()":'o','(al)':'al'}
        s=command.replace("G","G").replace("()",'o').replace("(al)","al")
        return s
            
        