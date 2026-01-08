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
        # If one of the lists are empty:
        if not list1 or not list2:
            return list1 if list1 else list2

        # Set first value
        if list1.val <= list2.val:
            new_list = ListNode(list1.val)
            list1 = list1.next
        else:
            new_list = ListNode(list2.val)
            list2 = list2.next

        current_new_node = new_list
        while list1 and list2:
            # Create new list node, set its value to whichever is less of the heads of the linked lists, moving whichever linked list head is less along
            new_node = ListNode()
            if list1.val <= list2.val:
                new_node.val = list1.val
                list1 = list1.next
            else:
                new_node.val = list2.val
                list2 = list2.next
            current_new_node.next = new_node
            current_new_node = current_new_node.next
    
        # Append the rest of the list; one of the lists is null
        current_new_node.next = list1 if list1 else list2

        return new_list