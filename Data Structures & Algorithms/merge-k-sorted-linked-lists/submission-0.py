# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def helper(head1, head2):
            if not head1:
                return head2
            if not head2:
                return head1

            temp = ListNode(-1)
            head = temp

            while head1 and head2:
                if head1.val <= head2.val:
                    head.next = head1
                    head1 = head1.next
                else:
                    head.next = head2
                    head2 = head2.next

                head = head.next

            if head1:
                head.next = head1
            if head2:
                head.next = head2

            return temp.next

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                head1 = lists[i]
                head2 = lists[i + 1] if i + 1 < len(lists) else None

                merged = helper(head1, head2)
                merged_lists.append(merged)

            lists = merged_lists

        return lists[0]
