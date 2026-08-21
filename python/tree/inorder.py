# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from git import List
from pyparsing import Optional
from python.common import TreeNode

from python.common.models import TreeNode


class Solution:
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
            res = []

            def inorder(cur):
                if cur:
                    inorder(cur.left)
                    res.append(cur.val)
                    inorder(cur.right)

            inorder(root)
            return res