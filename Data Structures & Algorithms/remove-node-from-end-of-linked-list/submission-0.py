# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        target_index = len(arr) - n

        if target_index == 0:
            return head.next
        
        prev_node = arr[target_index - 1]
        prev_node.next = prev_node.next.next

        return head