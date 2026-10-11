# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.checknode(root)
    def findHeight(self,node):
        if node is None:
            return 0
        lh = self.findHeight(node.left)
        rh = self.findHeight(node.right)

        return 1 + max(lh, rh)
    def checknode(self,node):
        if node==None:
            return True
        lh=self.findHeight(node.left)
        rh=self.findHeight(node.right)
        if abs(lh-rh)>1:
            return False
        left=self.checknode(node.left)
        right=self.checknode(node.right)
        if not left or not right:
            return False
        return True
    
            