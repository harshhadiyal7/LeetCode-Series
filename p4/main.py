#9. Palindrome Number
'''
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 1. Edge Cases:
        # Negative numbers are not palindromes (e.g., -121 reads 121-).
        # Numbers ending in 0 (other than 0 itself) cannot be palindromes (e.g., 10 reads 01).
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        # 2. Reversing the number mathematically
        reversed_num = 0
        temp = x
        
        while temp > 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10  # Integer division to remove the last digit
            
        # 3. Check if the reversed number equals the original
        return x == reversed_num