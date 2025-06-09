"""
Title: 20. Valid Parentheses
URL: https://leetcode.com/problems/valid-parentheses/
Constraints:
  - 1 <= s.length <= 104
  - s consists of parentheses only '()[]{}'.
Complexity: O(n) time, O(n) space
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for char in s:
        if char not in pairs:
            stack.append(char)
        else:
            if not stack or pairs[char] != stack[-1]: return False
            stack.pop()
    return not stack