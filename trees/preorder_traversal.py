from typing import List, Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Iterative solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            current = stack.pop()  # Process current node
            result.append(current.val)
            # Push right first (processed later)
            if current.right:
                stack.append(current.right)
            # Push left last (processed next)
            if current.left:
                stack.append(current.left)
        
        return result