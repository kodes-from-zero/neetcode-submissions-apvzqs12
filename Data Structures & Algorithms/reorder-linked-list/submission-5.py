# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return 
        slow, fast = head , head
        l1 = head
        prev=None
        while fast and fast.next:
            prev=slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        l2=slow
        prev_1 = None
        curr = l2
        while curr:
            temp = curr.next
            curr.next = prev_1
            prev_1 = curr
            curr = temp
        l2=prev_1
        dummy = ListNode()
        tail=dummy
        while l1 and l2:
            tail.next = l1
            tail=tail.next
            l1= l1.next
            tail.next = l2
            tail=tail.next
            l2=l2.next
        tail.next = l1 if l1 else l2


     
        