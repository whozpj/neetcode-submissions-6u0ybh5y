# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        curr = head

        def reverseNextBatch(curr):
            numReversed = 0
            prev = None
            while numReversed < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                numReversed += 1

            return prev, curr #prev is the last of the reversed, curr is the start of next group

        def isValid(curr):
            for i in range(k):
                if curr:
                    curr = curr.next
                else:
                    return False
            return True

        dummy = ListNode()
        dummy.next = head
        prevGroupEnding = dummy
        

        while isValid(prevGroupEnding.next):

            groupStart = prevGroupEnding.next

            newHead, nextGroup = reverseNextBatch(groupStart)

            # connect previous part -> reversed head
            prevGroupEnding.next = newHead

            # connect tail of reversed group -> next group
            groupStart.next = nextGroup

            # move prevGroupEnding forward
            prevGroupEnding = groupStart

        return dummy.next
        