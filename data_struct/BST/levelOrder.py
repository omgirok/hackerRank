def levelOrder(self,root):
    h = self.getHeight(root)+1
    for i in range(1, h+1):
        thisLevel=self.printLevelOrder(root,i)

def printLevelOrder(self, root, height):
    if root is None:
        return
    if height == 1:
        print "%d" %(root.data),
    elif height > 1:
        self.printLevelOrder(root.left, height-1)
        self.printLevelOrder(root.right, height-1)

def getHeight(self,root):
    # no height if only root exists and has no children
    if root == None:
        return 0
    if root.left is None and root.right is None:
        return 0

    hleft = self.getHeight(root.left)
    hright = self.getHeight(root.right)
    height = 1 + max(hleft,hright)
    return height