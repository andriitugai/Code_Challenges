# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p = head
        count = 0
        while p:
            count += 1
            if count == k:
                p1 = p

            p = p.next

        p = head
        c = 0
        while c < count - k:
            c += 1
            p = p.next

        p2 = p

        p1.val, p2.val = p2.val, p1.val

        return head
