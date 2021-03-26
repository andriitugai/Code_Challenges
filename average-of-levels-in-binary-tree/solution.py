# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        from queue import SimpleQueue
        q = SimpleQueue()
        q.put(root)
        result = []
        while not q.empty():
            level_size = q.qsize()
            level_sum = 0
            for _ in range(level_size):
                node = q.get()
                level_sum += node.val
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

            result.append(level_sum / level_size)

        return result