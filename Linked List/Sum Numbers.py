# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        elif l2==None:
            return l1
        h1,h2 = l1,l2
        carry = 0
        x = ListNode()
        x.next = l2
        while h1!=None and h2!=None:
            val = (h1.val+h2.val+carry)%10
            carry = (h1.val+h2.val+carry)//10
            h2.val = val
            tail = h2
            h2 = h2.next
            h1 = h1.next
        if h1!=None:
            tail.next = h1
            while h1 and carry:
                val = (h1.val+carry)%10
                carry = (h1.val+carry)//10
                h1.val = val
                tail = h1
                h1 = h1.next
        if h2!=None:
            while h2 and carry:
                val = (h2.val+carry)%10
                carry = (h2.val+carry)//10
                h2.val = val
                tail = h2
                h2 = h2.next
        if carry:
            last = ListNode(1,None)
            tail.next = last
        return x.next