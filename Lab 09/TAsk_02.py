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
    
    # Post-order traversal
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)
    
    # Print the BST
    def print_bst(self):
        self._print_bst(self, 0)
    
    def _print_bst(self, node, level):
        if node is not None:
            self._print_bst(node.right, level + 1)
            print('    ' * level + str(node.data))
            self._print_bst(node.left, level + 1)

# Create the BST and insert elements
root = BST(54)
root.insert(34)
root.insert(46)
root.insert(12)
root.insert(23)
root.insert(5)
root.insert(18)
root.insert(80)

print("Post-order Traversal of Binary Search Tree:")
root.postorder()

print("BST Structure:")
root.print_bst()
