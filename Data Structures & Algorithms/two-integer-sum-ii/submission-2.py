class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i,n in enumerate(numbers):
        #     diff = target-n
        #     if diff in numbers and numbers.index(diff)!= i:
        #         return sorted([i+1,numbers.index(diff)+1])

        #optimal solution from NC vid
        left = 0
        right = len(numbers) -1
        while left<right and right < len(numbers):
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left+1, right+1]
            elif curr > target:
                right -=1
            elif curr < target:
                left +=1 
        return [left+1, right+1] 
        