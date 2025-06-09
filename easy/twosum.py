"""
Title: 1. Two Sum
URL: https://leetcode.com/problems/two-sum/
Constraints:
  - 2 <= nums.length <= 104
  - -109 <= nums[i] <= 109
  - -109 <= target <= 109
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
Complexity:
  - twoSumNaive: O(n^2) time, O(1) space
  - twoSum: O(n) time, O(n) space
"""

def twoSumNaive(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(nums):
        for j in range(nums):
            if i != j and nums[i] + nums[j] == target:
                return i, j
    return None

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return nums_dict[complement], i
        else:
            nums_dict[num] = i
        
    return None