# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def findheight(node):
            if node is None:
                return 0
            lh=findheight(node.left)
            rh=findheight(node.right)
            self.diameter=max(self.diameter,lh+rh)
            return 1+max(lh,rh)
    
        findheight(root)
        return self.diameter

        