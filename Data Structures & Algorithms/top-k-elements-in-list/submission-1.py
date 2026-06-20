from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        # dict with num : count
        # make enumerated list of counts(values)
        # find top k numbers, and get their index numbers
        # get keys at index numbers found and append that into a list
        nums_counts = dict()
        for i in nums:
            if i in nums_counts:
                nums_counts[i] = nums_counts[i] + 1
            else:
                nums_counts[i] = 1

        keys = list(nums_counts.keys())
        values = enumerate(list(nums_counts.values()))

        sorted_vals = list(reversed(sorted(values, key=lambda x:x[1])))

        # for i,j in sorted_vals:
        #     print(i,j)

        for i in range(k):
            output.append(keys[sorted_vals[i][0]])
        return output