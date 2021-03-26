# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(val=v, left=root)

        from queue import SimpleQueue
        q = SimpleQueue()
        level = 1
        q.put(root)
        while level < d - 1:
            for _ in range(q.qsize()):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            level += 1

        while not q.empty():
            node = q.get()
            node.left = TreeNode(val=v, left=node.left)
            node.right = TreeNode(val=v, right=node.right)

        return root
