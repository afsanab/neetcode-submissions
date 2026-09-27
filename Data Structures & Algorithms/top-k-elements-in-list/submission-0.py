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

        top_k = nlargest(k, values)

        for i in top_k:
            output.append(keys[i[0]])

        return output