# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def val_to_list(self, node) : 
        ls = []
        while node : 
            ls.append(node.val)
            node = node.next

        return ls
    
    
    def make_linked_list(self, ls) : 
        if ls == [] : 
            return None
        node = ListNode(val = ls[0])
        next = node
        for i in range(1, len(ls)) : 
            next.next = ListNode(val = ls[i])
            next = next.next
            
        return node
    
    
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lsReverse = self.val_to_list(head)[::-1]
        print(lsReverse)
        return self.make_linked_list(lsReverse)
        