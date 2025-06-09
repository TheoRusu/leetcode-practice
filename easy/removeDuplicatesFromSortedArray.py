"""
Title: 26. Remove Duplicates from Sorted Array
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Constraints:
  - 1 <= nums.length <= 3 * 104
  - -100 <= nums[i] <= 100
  - nums is sorted in non-decreasing order.
Complexity: O(n) time, O(1) space
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k