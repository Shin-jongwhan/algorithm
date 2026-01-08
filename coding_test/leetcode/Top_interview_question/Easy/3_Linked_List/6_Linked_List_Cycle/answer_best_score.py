# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        """
        while current_node != None:
            check dict keys for current node
            if present, return true
            add current node to dictionary
            current node = current node.next

        return false
        """
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow is not None and fast is not None:
            if slow is fast:
                return True
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False
        
        return False