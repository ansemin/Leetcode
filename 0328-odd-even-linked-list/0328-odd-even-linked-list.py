# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0,; next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_tail=head # points to the first element
        even_tail=head.next # points ot the second eleent 
        odd_head=head
        even_head=head.next
        while even_tail and even_tail.next is not None:
            odd_tail.next=even_tail.next
            odd_tail=odd_tail.next
            even_tail.next=odd_tail.next
            even_tail=even_tail.next
        odd_tail.next=even_head # connect this to the beginning of the even_tail
        return odd_head #return the head of the odd_tail