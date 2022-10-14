# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head.next:
#             return None
        
#         total, count = 0, 0
#         curr = head
#         midd = head
#         prev = None
#         while curr:
#             if ((total+1)//2) > count:
#                 prev = midd
#                 midd = midd.next
#                 count += 1
#             curr = curr.next
#             total += 1
        
#         temp = midd.next
#         prev.next = temp
        
#         return head

        if not head.next:
            return head.next

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            if not fast or not fast.next:
                slow.next = slow.next.next
            else:
                slow = slow.next

        return head