# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the midpoint of the list
        dummy = head
        slowpointer = dummy
        fastpointer = dummy

        while fastpointer != None:
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next

        # Now slowpointer marks the halfway point
        dummy = head
        current = dummy
        prev = slowpointer
        nextlocation = current.next
        
        while current != slowpointer:
            current.next = prev
            prev = current
            current = nextlocation
            nextlocation = current.next

        dummy = prev
        cursor1 = dummy
        cursor2 = slowpointer
        maximum_seen = 0

        while cursor2 != None:
            sum_of_pointers = cursor1.val + cursor2.val
            if sum_of_pointers > maximum_seen:
                maximum_seen = sum_of_pointers
            cursor1 = cursor1.next
            cursor2 = cursor2.next
            
        return maximum_seen