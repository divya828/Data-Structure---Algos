# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        h1,h2 = list1,list2
        if h1==None:
            return h2
        elif h2==None:
            return h1
        if h1.val>h2.val:
            t = h2
            h2 = h2.next
        else:
            t = h1
            h1 = h1.next
        x = ListNode()
        x.next = t
        while h1 and h2:
            if h1.val>h2.val:
                t.next = h2
                h2 = h2.next
            else:
                t.next = h1
                h1 = h1.next
            t = t.next
        if h1:
            t.next = h1
        elif h2:
            t.next = h2
        return x.next