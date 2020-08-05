"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict 
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: 
            return []    
        answer = defaultdict(list) 
        answer[0] = [root.val]
        res = []
        queue = [[root,0]]
        while queue:
            node, layer = queue.pop(0)
            if node.left:
                answer[layer+1].append(node.left.val)
                queue.append((node.left, layer+1))
            if node.right:
                answer[layer+1].append(node.right.val)
                queue.append((node.right, layer+1))
        
        for key, lst in answer.items():
            if(key % 2 == 0):
                res.append(lst)
            else:
                res.append(lst[::-1])
        
        return res