def getHeight(self,root):
    #Write your code here
    if root == None:
        return 0
    if root.left is None and root.right is None:
        return 0
    
    hleft = self.getHeight(root.left)
    hright = self.getHeight(root.right)
    
    height = 1 + max(hleft,hright)
    return height
