# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_len(node) : 
	n = 0
	while node : 
		n += 1
		node = node.next
	
	return n


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        print(head)
        length = get_len(head)
        print(length)
        
        idx = length - (n - 1)
        current = head
        prev = None
        
        # 가장 첫 번째이면 바로 return한다.
        if n == length : 
            return current.next
        
        nCount = 0 
        while current : 
            nCount += 1 
            if nCount == idx :
                prev.next = prev.next.next
                break
            prev = current
            current = current.next

        return head
        
        