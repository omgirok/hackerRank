# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    row=[]
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result=[]
        h = self.getHeight(root)+1
        for i in range(1, h+1):
            self.row=[]
            print "iteration:",i
            self.makeLevelOrder(root,i)
            result.append(self.row)
        return result
        
    def makeLevelOrder(self, root, height):
        if root is None:
            return
        if height == 1:
            self.row.append(root.val)
            return
        elif height > 1:
            leftEle = self.makeLevelOrder(root.left, height-1)
            rightEle = self.makeLevelOrder(root.right, height-1)

    def getHeight(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        height = 0
        
        hleft = self.getHeight(root.left)
        hright = self.getHeight(root.right)
        height = 1 + max(hleft,hright)
        return height