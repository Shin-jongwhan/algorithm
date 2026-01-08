# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root : 
            return []

        depth = 1
        dq = deque([(root, depth)])
        ls = []
        while dq : 
            node, depth = dq.popleft()
            if node.left : 
                dq.append((node.left, depth + 1))
            if node.right : 
                dq.append((node.right, depth + 1))
            if len(ls) == depth : 
                ls[-1].append(node.val)
            else : 
                ls.append([node.val])

        return ls