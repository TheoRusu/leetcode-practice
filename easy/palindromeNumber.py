# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
# Constraints:
# -231 <= x <= 231 - 1
 
# Follow up: Could you solve it without converting the integer to a string?


# O(log x)) time complexity, O(log x) space complexity
def isPalindromeStringConvert(x):
    """
    :type x: int
    :rtype: bool
    """
    s = str(x)
    return s == s[::-1]


# O(log x)) time complexity, O(1) space complexity
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10

    return x == rev or x == rev // 10