class Solution:
    #get len of strs, then have first be number then the word
    #combine the strings all to be a big string, then get the individual 
    #strings back

    def encode(self, strs: List[str]) -> str:
        #wrote this func myself
        output = []
        for s in strs:
            output.append(str(len(s)))
            output.append("#")
            output.append(s)
        output = "".join(output)
        print(output)
        return output
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # the nums before # is the num letters
            length = int(s[i:j])
            #update i to be before the string we are adding now - skipping nums/#
            i = j + 1
            #update j to be after the string
            j = i + length
            # from indexes i - j is the actual string value
            res.append(s[i:j])
            #update both to be at end of string
            i = j
            
        return res