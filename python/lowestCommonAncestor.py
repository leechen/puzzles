# Definition for a binary search tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p or not q:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p , q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

        return self.lowestCommonAncestor(root, p, q)

    def lowestCommonAncestorIter(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur