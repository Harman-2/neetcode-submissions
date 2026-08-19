# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next # save the reference
            curr.next = prev # flip the pointer
            prev = curr # shift prev forward
            curr = nxt # shift curr forward
        return prev