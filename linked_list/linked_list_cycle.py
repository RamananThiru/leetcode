
"""

https://leetcode.com/problems/linked-list-cycle/description/

This solution was accepted. But a different algorithm is present for linked-list-cycle. Please read that 


Ref link: https://takeuforward.org/data-structure/detect-a-cycle-in-a-linked-list/ 
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        hash  = {}


        while(head.next is not None):
            
            if head.next in hash:
                return True

            hash[head.next] = head.val
            head = head.next
        return False    
        
