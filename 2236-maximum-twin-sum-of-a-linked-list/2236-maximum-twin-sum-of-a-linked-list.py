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
        # print(elements) #[5, 4, 2, 1]
        # total length
        n=len(elements)
        maximum=0
        for i in range(n):
            pair=n-1-i
            # print(f'i: {i}')
            # print(f' pair is {pair}')
            # print(type(pair))
            total=elements[pair]+elements[i]
            # print(total)
            maximum=max(total,maximum)
        return maximum 


