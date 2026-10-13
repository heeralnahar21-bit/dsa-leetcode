# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        ans=[]
        left_to_right=True
        queue=deque([root])
        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if not left_to_right :
                level.reverse()
            ans.append(level)
            left_to_right=not left_to_right
        return ans

        