# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if(head.next == None):
            return head
        node = head.next
        current = head
        value = head.val
        while(node.next):
            if(node.val == value):
                current.next = node.next
                node = node.next
            else:
                current = node
                value = node.val
                node = node.next
        if(node.val == value):
            current.next = None
        return head
            