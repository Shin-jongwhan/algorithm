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
        elif head and not head.next : 
            return True
        ls = [head.val]
        current = head.next

        while current : 
            ls.append(current.val)
            current = current.next

        for i in range(0, int(len(ls) / 2)) : 
            if ls[i] != ls[-i-1] : 
                return False

        return True