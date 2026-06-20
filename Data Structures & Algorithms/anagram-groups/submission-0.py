class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through each string, sort them, if the sorted key is found in the dictionary
        # then add the unsorted str to the value list
        # if key not found in dict, add it and create a list for value with unsorted str
        groups = {}
        for i in strs:
            if ''.join(sorted(i)) in groups:
                groups[''.join(sorted(i))].append(i)
            else:
                groups[''.join(sorted(i))] = [i]
        return list(groups.values())
            