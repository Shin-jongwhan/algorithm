# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root or (root.left and not root.right) or (root.right and not root.left) : 
            return False
        if root.left is None and root.right is None : 
            return True
        try : 
            stack = [(root.left, root.right)]
        except : 
            return False

        while stack : 
            left, right = stack.pop()
            if left.val == right.val : 
                if left.left and right.right : 
                    stack.append((left.left, right.right))
                elif not left.left and not right.right : 
                    pass
                else : 
                    return False
                if left.right and right.left : 
                    stack.append((left.right, right.left))
                elif not left.right and not right.left : 
                    pass
                else : 
                    return False
            else : 
                return False

        return True