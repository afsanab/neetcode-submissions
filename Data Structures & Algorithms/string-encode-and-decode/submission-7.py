class Solution:
    #get len of strs, then have first be number then the word
    #combine the strings all to be a big string, then get the individual 
    #strings back

    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append("#")
            output.append(str(len(s)))
            output.append(s)
        output = "".join(output)
        return output
    
    def decode(self, s: str) -> List[str]:
        index = 0
        res = []
        while index < len(s):
            #"#"
            if s[index] == "#" and s[index + 1].isnumeric():
                count = int(s[index+1])
                index +=2
                temp_str = ""
                for i in range(0,count):
                    temp_str += s[index + i]
                res.append(temp_str)
                index += count
            else:
                index +=1
        return res