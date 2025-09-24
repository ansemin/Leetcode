# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        prev=None
        curr=slow

        while curr:
            nextnode=curr.next #save
            curr.next=prev #move curr.next
            prev=curr # move prev
            curr=nextnode

        head2=prev
        maximum=0
        while head2:
            maximum=max(maximum, head2.val+head.val)
            head=head.next
            head2=head2.next
        return maximum 
