"""
Title: 14. Longest Common Prefix
URL: https://leetcode.com/problems/longest-common-prefix/
Constraints:
  - 1 <= strs.length <= 200
  - 0 <= strs[i].length <= 200
  - strs[i] consists of only lowercase English letters if it is non-empty.
Complexity: O(n*m) time where m is length of first string, O(1) space
"""

def longestCommonPrefix(strs: list[str]):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
