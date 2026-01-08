# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def create_linked_list(self, ls) : 
        if ls == [] : 
            return None
        ln = ListNode(ls[0])
        next = ln
        for i in range(1, len(ls)) : 
            next.next = ListNode(ls[i])
            next = next.next
            
        return ln
    
    
    def val_to_list(self, node) : 
        ls = []
        while node : 
            ls.append(node.val)
            node = node.next
            
        return ls
    
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lsConvert1 = self.val_to_list(list1)
        lsConvert2 = self.val_to_list(list2)
        lsConcat = sorted(lsConvert1 + lsConvert2)
        print(lsConcat)
        lnConcat = self.create_linked_list(lsConcat)
        print(lnConcat)
        return lnConcat
        
        
        