# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       #step-1: Find the middle and split the list into 2 halves:
       if head.next == None:
            return
       slow, fast, l1 = head, head, head
       prev = None
       while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
       if prev:
            prev.next=None
       #step-2 reverse the 2nd list from slow 
       curr = slow
       prev_1=None
       while curr:
            temp = curr.next
            curr.next = prev_1
            prev_1 = curr
            curr = temp
       l2=prev_1
       #3 join both lists 
       dummy = ListNode()
       tail = dummy
       while l1 and l2:
            tail.next = l1
            l1=l1.next
            tail=tail.next
            tail.next=l2
            l2=l2.next
            tail=tail.next
       tail.next = l1 if l1 else l2
       if dummy:
            head = dummy.next
    









       