# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #first, find the midpoint of the list (slow fast pointer approach) - Done
        #Create two lists, l1 and l2, first half, second half - done
        #reverse l2
        #merge together into a new list as final answer

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        l1 = head
        l2 = slow.next
        slow.next = None


        prev = None
        curr = l2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l2 = prev
        
        while l2:
            inter = l2.next
            temp = l1.next
            l1.next = l2
            l2.next = temp
            l2 = inter
            l1 = l1.next.next







        