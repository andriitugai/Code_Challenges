# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head

        head_lt, head_ge = None, None
        p_lt, p_ge = None, None

        p = head
        while p:
            if p.val < x:
                if not p_lt:
                    head_lt = ListNode(val=p.val)
                    p_lt = head_lt
                else:
                    p_lt.next = ListNode(val=p.val)
                    p_lt = p_lt.next
            else:
                if not p_ge:
                    head_ge = ListNode(val=p.val)
                    p_ge = head_ge
                else:
                    p_ge.next = ListNode(val=p.val)
                    p_ge = p_ge.next

            p = p.next

        if p_lt:
            p_lt.next = head_ge
            return head_lt

        return head_ge

