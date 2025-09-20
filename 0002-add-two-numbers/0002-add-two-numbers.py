# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # define the head
        cursor1=l1
        cursor2=l2
        # create result dummy
        result=ListNode()
        tail=result
        # initiate the carry value 
        carry=0
        while cursor1 is not None or cursor2 is not None or carry!=0:
            # Extract values : if it's empty then set it default as zero 
            # This is to set values as zero for different len of lists
            value1=cursor1.val if cursor1 else 0
            value2=cursor2.val if cursor2 else 0
            summed=value1+value2+carry
            carry=summed//10
            digit=summed%10 

            tail.next=ListNode(digit)
            tail=tail.next

            cursor1=cursor1.next if cursor1 else None

            cursor2=cursor2.next if cursor2 else None
        return result.next 




