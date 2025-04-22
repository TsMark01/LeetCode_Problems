# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2) :
        result = last_node = ListNode()
        addition = 0
        while l1 or l2 or addition:

            summ = addition

            if l1:
                summ += l1.val
                l1 = l1.next

            if l2:
                summ += l2.val
                l2 = l2.next


            addition = summ // 10

            last_node.next = ListNode(summ % 10)
            last_node = last_node.next
        return result.next