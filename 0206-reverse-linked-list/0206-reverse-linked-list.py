# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        prev=None
        cursor=head
        while cursor:
            next_=cursor.next
            cursor.next=prev
            prev=cursor
            cursor=next_
        return prev