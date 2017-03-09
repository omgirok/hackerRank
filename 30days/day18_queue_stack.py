class Solution:
    """ need queue and stack objects here """
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, c):
        self.stack.append(c)
        return

    def popCharacter(self):
        c = self.stack.pop()
        return c

    def enqueueCharacter(self, c):
        self.queue.append(c)
        return

    def dequeueCharacter(self): 
        c = self.queue.pop(0)
        return c