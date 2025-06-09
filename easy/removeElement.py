"""
Title: 27. Remove Element
URL: https://leetcode.com/problems/remove-element/
Constraints:
  - 0 <= nums.length <= 100
  - 0 <= nums[i] <= 50
  - 0 <= val <= 100
Complexity: O(n) time, O(1) space
"""

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i], nums[k] = nums[k], nums[i]
            k += 1
    return k