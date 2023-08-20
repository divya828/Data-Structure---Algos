# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = ListNode()
        x = ListNode()
        x.next = head
        fast,slow.next = head,head
        for i in range(n):
            fast=fast.next
        if fast==None:
            return head.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next = slow.next.next
        return x.next