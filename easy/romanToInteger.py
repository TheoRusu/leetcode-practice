"""
Title: 13. Roman to Integer
URL: https://leetcode.com/problems/roman-to-integer/
Constraints:
  - 1 <= s.length <= 15
  - s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
  - It is guaranteed that s is a valid roman numeral in the range [1, 3999].
Complexity: O(n) time, O(1) space
"""

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            num -= roman_dict[s[i]]
        else:
            num += roman_dict[s[i]]
    return num