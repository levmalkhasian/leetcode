# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        if root == None:  # if there is no root, just return empty list
            return [] 
        stack = [root] # stack definition with root to start with (LIFO)

        while stack: # loop until stack is empty ( [] )
            canidate = stack.pop() # removes top node from stack
            result.append(canidate.val) # add that node value to result

            if canidate.right:  # checks for children and adds to stack, then loop back once done
                stack.append(canidate.right)
            if canidate.left:
                stack.append(canidate.left)
        
        return result # return final list