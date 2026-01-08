# leetcode 답안
# 위에서부터 아래로 순차적으로 각 자식 노드를 맞바꾼다. 이걸 반복하면 각 전체 행이 뒤집어진다.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None : 
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root