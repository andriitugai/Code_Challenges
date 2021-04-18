# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        n_fast = head
        n_slow = head

        count = -1

        while n_fast:
            n_fast = n_fast.next
            count += 1
            if count > n:
                n_slow = n_slow.next

        if n_slow == head and count == n - 1:
            return head.next

        n_slow.next = n_slow.next.next
        return head
