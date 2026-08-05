# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return None
            
        q = head.next
        p = head
        head.next = None

        while q:
            temp = q.next
            q.next = p
            p = q
            q = temp

        return p

