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
        left = 0
        
        while left < len(s):
            right = left
            while s[right] != '#':
                right += 1
            # the nums before # is the num letters
            length = int(s[left:right])
            #update i to be before the string we are adding now - skipping nums/#
            left = right + 1
            #update j to be after the string
            right = left + length
            # from indexes left -> right is the actual string value
            res.append(s[left:right])
            #update both to be at end of string
            left = right
            
        return res