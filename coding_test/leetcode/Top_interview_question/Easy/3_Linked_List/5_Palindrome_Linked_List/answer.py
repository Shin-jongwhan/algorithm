from collections import deque

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head : 
            return False
        dq1 = deque([])
        dq2 = deque([])
        current = head

        while current : 
            dq1.append(current.val)
            dq2.appendleft(current.val)
            current = current.next

        print(dq1)
        print(dq2)
        return dq1 == dq2