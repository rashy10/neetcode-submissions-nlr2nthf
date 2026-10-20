# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1,None)
        start = temp
        if not list1:
            return list2
        if not list2:
            return list1

        while list1 and list2 :
            if list1 and list2 and (list1.val <= list2.val):
                start.next = list1
                start = start.next
                list1 = list1.next
            else:
                start.next = list2
                start = start.next
                list2 = list2.next
        if list1 :
            start.next = list1
        if list2:
            start.next = list2

        return temp.next

        