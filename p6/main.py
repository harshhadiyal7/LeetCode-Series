# 189. Rotate Array(Medium)
'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle cases where k > array length
        
        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # 1. Reverse the whole thing: [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
        reverse(0, n - 1)
        
        # 2. Reverse the first k elements: [7,6,5, 4,3,2,1] -> [5,6,7, 4,3,2,1]
        reverse(0, k - 1)
        
        # 3. Reverse the rest: [5,6,7, 4,3,2,1] -> [5,6,7, 1,2,3,4]
        reverse(k, n - 1)
