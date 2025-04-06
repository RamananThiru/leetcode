input_arr = [1,2,3,4,5,6,7,8,9]

"""
link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Notes:
- Inorder traversal is done on a built tree
- General you assume the given array is in order of the tree built


"""


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None



# Recursive solution - Had the solution in my head , lack clarity
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        result = result + self.inorderTraversal(root.left)
        result.append(root.val)
        result = result + self.inorderTraversal(root.right)

        return result







