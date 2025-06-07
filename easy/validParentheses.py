# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# O(n) time complexity, O(n) space complexity
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