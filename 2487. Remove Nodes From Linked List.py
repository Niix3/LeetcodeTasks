# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: [ListNode]) -> [ListNode]:
        def reverse(nodeHead):#reverse of a linked list
            prev = None
            curr = nodeHead
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        reverse_head = reverse(head)
        max_elem = reverse_head.val
        current = reverse_head
        while current.next:
            if current.next.val < max_elem:
                current.next = current.next.next
            else:
                max_elem = current.next.val
                current = current.next
        return reverse(reverse_head)