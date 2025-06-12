"""
Title: 35. Search Insert Position
URL: https://leetcode.com/problems/search-insert-position/
Constraints:
  - 1 <= nums.length <= 104
  - -104 <= nums[i] <= 104
  - nums contains distinct values sorted in ascending order.
  - -104 <= target <= 104
Complexity: O(log n) time, O(1) space
"""

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left