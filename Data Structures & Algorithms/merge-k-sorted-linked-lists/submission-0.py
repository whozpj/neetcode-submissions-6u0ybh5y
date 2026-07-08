# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoLists(list_1, list_2): #inputs are heads of linked lists

            dummy = ListNode()
            curr = dummy

            while list_1 or list_2:

                if list_1 and list_2:
                    if list_1.val < list_2.val:
                        curr.next = list_1
                        list_1 = list_1.next
                        curr = curr.next

                    else:
                        curr.next = list_2
                        list_2 = list_2.next
                        curr = curr.next
                elif list_1:
                    curr.next = list_1
                    list_1 = list_1.next
                    curr = curr.next
                elif list_2:
                    curr.next = list_2
                    list_2 = list_2.next
                    curr = curr.next
            return dummy.next

        prevList = None
        for lis in lists:
            prevList = mergeTwoLists(prevList, lis)
        return prevList

