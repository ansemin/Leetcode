# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handle edge cases or single element cases 
        if not head or head.next is None:
            return head 
        # cursor=head
        # result=ListNode()
        # tail=result
        # while cursor and cursor.next is not None:
        #     nxt=cursor.next
        #     tail.next=tail
        #     tail=nxt
        #     cursor=cursor.next 
        # return head

        prev=None
        curr=head
        while curr:
            next_temp=curr.next
            curr.next=prev
            prev=curr
            curr=next_temp
        return prev
