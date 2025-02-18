#Remove Nth Node From End of List

#Write a function solve that removes the nth node from the end of a singly linked list. Return the head.

#Example:
#Input: [1,2,3,4,5], 2
#Output: [1,2,3,5] 

#Make sure you return your solution, don't print!


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def solve(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next




