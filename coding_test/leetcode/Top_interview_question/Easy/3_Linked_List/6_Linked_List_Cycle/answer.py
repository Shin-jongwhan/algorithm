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
        if not head : 
            return False

        stAddress = set([id(head)])
        current = head

        while current : 
            if id(current.next) not in stAddress : 
                stAddress.add(id(current.next))
            else : 
                return True
            current = current.next

        return False