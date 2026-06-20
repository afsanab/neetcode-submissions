class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through each string, sort them, if the sorted key is found in the dictionary
        # then add the unsorted str to the value list
        # if key not found in dict, add it and create a list for value with unsorted str
        groups = dict()
        for i in strs:
            #''.join(sorted(i)) used to put the sorted letters back into a string format
            if ''.join(sorted(i)) in groups:
                #add unsorted string to the values list
                groups[''.join(sorted(i))].append(i)
            else:
                #create a list with the unsorted values, sorted as key
                groups[''.join(sorted(i))] = [i]
        #resturn list of dict values
        return list(groups.values())
            