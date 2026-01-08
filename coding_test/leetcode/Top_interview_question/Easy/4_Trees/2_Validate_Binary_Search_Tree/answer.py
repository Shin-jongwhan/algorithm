# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root : 
            return False
        stack = [(root, -(2 ** 31) - 1, 2 ** 31)]		# node, 최솟값, 최댓값
        while stack : 
            node, low, high = stack.pop()
            if node is not None : 
                if node.left is not None : 
                    if node.val <= node.left.val or low >= node.left.val or high <= node.left.val : 
                        # low < node.left.val < node.val < high인지 검사
                        return False
                    stack.append((node.left, low, node.val))
                if node.right is not None : 
                    if node.val >= node.right.val or low >= node.right.val or high <= node.right.val : 
                        # low < node.val < node.right.val < high인지 검사
                        return False
                    stack.append((node.right, node.val, high))

        return True