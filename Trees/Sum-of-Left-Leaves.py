#Given the root of a binary tree, return the sum of all left leaves.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(not root or (not root.left and not root.right)):
            return 0
        
        count = 0
        node = root
        stack = []
        while(node or stack):
            if not node:
                node = stack.pop()
            else:
                while node.left:
                    stack.append(node)
                    node = node.left
            if(not node.right and not node.left and node!=root):
                count = count + node.val
            node = node.right
            if(node and (not node.right and not node.left)):
                count = count - node.val
                
        return count