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
            # Save the next node
            NextNode=cursor.next
            # Link it the next node to the prev
            cursor.next=prev
            # move the previous head to the current head
            prev=cursor
            # move the head to the updated head from the beginning
            cursor=NextNode
        return prev 