"""
Title: 28. Find the Index of the First Occurence in a String
URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Constraints:
  - 1 <= haystack.length, needle.length <= 104
  - haystack and needle consist of only lowercase English characters.
Complexity: O(n * m) time where n is length of haystack and m is length of needle, O(1) space
"""

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1