"""
Title: 21. Merge Two Sorted Lists
URL: https://leetcode.com/problems/merge-two-sorted-lists/
Constraints:
  - The number of nodes in both lists is in the range [0, 50].
  - -100 <= Node.val <= 100
  - Both list1 and list2 are sorted in non-decreasing order.
Complexity: O(n+m) time, O(1) space
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n + m) time complexity, O(1) space complexity
def mergeTwoLists(list1: ListNode, list2: ListNode):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = curr = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            curr.next, list1 = list1, list1.next
        else:
            curr.next, list2 = list2, list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2
    return dummy.next