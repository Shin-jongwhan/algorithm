# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 or not list2:
            return list1 if list1 else list2
        current1 = list1
        current2 = list2
        lnConcat = ListNode()
        next = lnConcat
        while current1 or current2 : 
            if current1 and current2 : 
                if current1.val >= current2.val : 
                    next.val = current2.val
                    current2 = current2.next
                else : 
                    next.val = current1.val
                    current1 = current1.next
            elif current1 : 
                next.val = current1.val
                current1 = current1.next
            elif current2 : 
                next.val = current2.val
                current2 = current2.next
            next.next = ListNode() if current1 or current2 else None
            next = next.next

        return lnConcat