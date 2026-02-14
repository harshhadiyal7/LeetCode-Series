#Two sum
'''
concept : 
nums = [5,9,1,2,4,15,6,3]
return index of target sum 2 numbers.
for ex: target=13  and 9 and 4 are numbers and we resturn index of 9 and 4. it means [1,4].
'''
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        pass