"""
Title: 9. Palindrome Number
URL: https://leetcode.com/problems/palindrome-number/
Constraints:
  - -231 <= x <= 231 - 1
Follow up: Could you solve it without converting the integer to a string?
Complexity:
  - isPalindromeStringConvert: O(log x) time, O(log x) space
  - isPalindrome: O(log x) time, O(1) space
"""

def isPalindromeStringConvert(x):
    """
    :type x: int
    :rtype: bool
    """
    s = str(x)
    return s == s[::-1]

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