# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: #not None == True
            return None
        fast=head
        slow=head
        prev=None # To track before middle 
        while fast and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next

        return head
