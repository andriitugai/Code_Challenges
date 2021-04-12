# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import SimpleQueue


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        #         def get_max_depth(root):
        #             if not root:
        #                 return 0
        #             return 1 + max(get_max_depth(root.left), get_max_depth(root.right))

        #         h = get_max_depth(root)
        q = SimpleQueue()
        q.put(root)
        while not q.empty():
            level_sum = 0
            for _ in range(q.qsize()):
                t = q.get()
                level_sum += t.val
                if t.left:
                    q.put(t.left)
                if t.right:
                    q.put(t.right)

        return level_sum
