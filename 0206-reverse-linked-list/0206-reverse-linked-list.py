# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases: an empty list or a list with only one node.
        # In these cases, the list is already "reversed", so we can return it as is.
        if not head or head.next is None:
            return head

        # Initialize the 'prev' pointer. It represents the "previous" node.
        # We start it at None because the original head will become the new tail,
        # and the tail of a linked list must point to None.
        prev = None
        
        # Initialize the 'cursor' (or 'current') pointer to the start of the list.
        # This is the node we will be processing in each iteration.
        cursor = head

        # Loop as long as the 'cursor' is not None. This ensures we process
        # every single node in the list, including the very last one.
        while cursor:
            # Step 1: Save the next node in the original list.
            # We must do this before we break the link, otherwise we'll lose
            # the rest of the list. Think of this as a temporary bookmark.
            next_element = cursor.next
            
            # Step 2: Reverse the pointer of the current node.
            # This is the core of the reversal. We make the current node's 'next'
            # pointer point backwards to whatever 'prev' was.
            cursor.next = prev
            
            # Step 3: Move the 'prev' pointer one step forward.
            # For the next iteration, our current node will be the "previous" one.
            # 'prev' now becomes the head of our reversed list so far.
            prev = cursor 
            
            # Step 4: Move the 'cursor' pointer one step forward.
            # We move to the node we saved in Step 1, allowing us to process
            # the next node in the original list.
            cursor = next_element
            
        # After the loop finishes, 'cursor' will be None, and 'prev' will be
        # pointing to the last node of the original list, which is now the
        # new head of the reversed list.
        return prev