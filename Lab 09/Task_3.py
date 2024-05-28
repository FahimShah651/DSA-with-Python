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
    
    # Delete a node from the BST
    def delete(self, key):
        if self.data is None:
            return self
        
        # If the key is smaller than the root's data, go left
        if key < self.data:
            self.left = self.left.delete(key)
        # If the key is greater than the root's data, go right
        elif key > self.data:
            self.right = self.right.delete(key)
        # If the key is equal to the root's data, delete the node
        else:
            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.right
            while temp.left is not None:
                temp = temp.left
            # Copy the inorder successor's content to the current node
            self.data = temp.data
            # Delete the inorder successor
            self.right = self.right.delete(temp.data)
        
        return self


# Create the BST and insert elements
root = BST(54)
root.insert(34)
root.insert(46)
root.insert(12)
root.insert(23)
root.insert(5)
root.insert(18)
root.insert(80)
root.insert(62)
root.insert(45)
root.insert(55)
root.insert(75)
root.insert(88)
root.insert(72)
root.insert(85)

print("BST Structure Before Deletion:")
root.print_bst()

# Delete a node from the BST
key_to_delete = 46
root = root.delete(key_to_delete)
print(f"Deleted node with key {key_to_delete}")

print("BST Structure After Deletion:")
root.print_bst()
