class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        ref = []
        #start with the last - it should always log to 0
        nxt = temperatures.pop()
        while temperatures:
            index = len(temperatures) - 1
            curr = temperatures[index]
            ref.append(nxt)
            #if next is warmer
            if curr < nxt:
                res[index] = 1
            #check ref from index of - this is the hard part
            else:
                count = 0
                for i in ref[::-1]:
                    count+=1
                    if i > curr:
                        # print(ref)
                        # print(curr)
                        # print(i)
                        # print(count)
                        res[index] = count
                        break
            nxt = temperatures.pop()
        return res

        