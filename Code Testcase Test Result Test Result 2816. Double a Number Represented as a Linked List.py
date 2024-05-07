# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head):
        def reverse(nodeHead):  # reverse of a linked list
            prev = None
            curr = nodeHead
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        reversed_node = reverse(head)
        carry = 0
        current, previous = reversed_node, None

        while current:
            new_value = current.val * 2 + carry
            current.val = new_value % 10
            carry = 1 if new_value > 9 else 0
            previous, current = current, current.next

        if carry:
            previous.next = ListNode(carry)

        result = reverse(reversed_node)

        return result