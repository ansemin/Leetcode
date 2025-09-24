# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cursor=head
        elements=[]
        while cursor:
            values=cursor.val
            elements.append(values)
            cursor=cursor.next
        n=len(elements)
        maximum=0
        j=n-1 
        i=0
        while i<j:
            total=elements[i]+elements[j]
            i+=1
            j-=1
            maximum=max(total,maximum) 
        return maximum


