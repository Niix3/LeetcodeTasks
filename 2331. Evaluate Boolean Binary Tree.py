# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # we'll use simple recursion
        if not root.left and not root.right:
            return root.val
        evaluate_left_subtree = self.evaluateTree(root.left)
        evaluate_right_subtree = self.evaluateTree(root.right)
        if root.val == 2:
            return evaluate_left_subtree or evaluate_right_subtree
        if root.val == 3:
            return  evaluate_left_subtree and evaluate_right_subtree