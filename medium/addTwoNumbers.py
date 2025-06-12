"""
Title: 2. Add Two Numbers
URL: https://leetcode.com/problems/add-two-numbers/
Constraints:
  - The number of nodes in each linked list is in the range [1, 100].
  - 0 <= Node.val <= 9
  - It is guaranteed that the list represents a number that does not have leading zeros.
Complexity: O(max(n,m)) time, O(max(n,m)) space
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = curr = ListNode()
    carry = 0

    while l1 or l2 or carry:
        l1num = l1.val if l1 else 0
        l2num = l2.val if l2 else 0
        total = l1num + l2num + carry

        carry = total // 10
        digit = total % 10

        curr.next = ListNode(digit)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next