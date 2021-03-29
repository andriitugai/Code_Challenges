# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        i = 0
        stack = [root]
        ans = []

        while stack:
            curr = stack.pop()
            if curr.val != voyage[i]:
                return [-1]

            i += 1
            if curr.left and curr.left.val != voyage[i]:
                curr.left, curr.right = curr.right, curr.left
                ans.append(curr.val)

            if curr.right:
                stack.append(curr.right)

            if curr.left:
                stack.append(curr.left)

        return ans



