'''https://leetcode.com/problems/add-two-numbers/'''

from math import floor


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l3 = ListNode(0)
        l3_tail = l3

        while l1 or l2 or carry:
            # add first two -> store value and carryover
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            value = total % 10
            carry = math.floor(total / 10)

            # add node to the chain and move chain to next node
            l3_tail.next = ListNode(value)
            l3_tail = l3_tail.next

            # move chains to next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return l3.next
