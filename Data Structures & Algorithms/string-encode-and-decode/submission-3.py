class Solution:
    #get len of strs, then have first be number then the word
    #combine the strings all to be a big string, then get the individual 
    #strings back

    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append("word_break")
            output.append(s)
        output = "".join(output)
        return output
    
    def decode(self, s: str) -> List[str]:
        s = s.split("word_break")[1:]
        return s
        