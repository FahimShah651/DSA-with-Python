class BST:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    # Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    # Print the tree
    def Preorder(self):
        print(self.data)
        if self.left:
            self.left.Preorder()
        if self.right:
            self.right.Preorder()

root = BST(54)
root.insert(34)
root.insert(46)
root.insert(12)
root.insert(23)
root.insert(5)

print("Preorder Traversal of Binary Search Tree: ")
root.Preorder()
