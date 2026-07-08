# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False
        slowCurrent = head
        if head.next:
            fastCurrent = head.next
        else: return False

        while slowCurrent and fastCurrent and fastCurrent.next:
            if slowCurrent == fastCurrent:
                return True
            slowCurrent = slowCurrent.next
            fastCurrent = fastCurrent.next.next
        return False