# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        left = head
        right = prev

        temp = ListNode(-1,None)
        new = temp
        flag = 0
        while left and right:
            if not flag:
                new.next = left
                new = new.next
                left = left.next
                flag = 1
            else:
                new.next = right
                new = new.next
                right = right.next
                flag = 0
        head = temp.next


        