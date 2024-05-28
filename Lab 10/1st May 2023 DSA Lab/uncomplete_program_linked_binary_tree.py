class LinkedBinaryTree:

    class Node:

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        

    def _validate(self, p):
        """Return associated node if position is valid."""
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        print("value of p="+str(p))
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        if node is not None:
           # print("i am inside make_position and value of node="+str(node))
            return self.Position(self, node)
        else:
            return None
        
       #. return self.Position(self, node) if node is not None else None

    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:   # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1
        return count

    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position."""
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self.Node(e)
        print(self._root)
        return self._make_position(self._root)

    def add_left(self, p, e):
        print("\n \nvalue of position = "+str(p))
        node = self._validate(p)
        print("\n \nvalue of node="+str(node))

        print("\n \n ******** \nvalue of node left="+str(node._left))

        if node._left is not None:
            raise ValueError("Left child exists")
        self._size += 1
        node._left = self.Node(e, node)
        return self._make_position(node._left)

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e."""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self.Node(e, node)
        return self._make_position(node._right)


    def replace(self, p, e):
        """Replace the element at position p with e, and return the old element."""
        
    def display_tree(self):
        """Display the binary tree."""
        

# main
# Create an instance of the LinkedBinaryTree
tree = LinkedBinaryTree()

# Add the root node
root_position = tree.add_root(1)
# print("root position is"+str(root_position))

# Add left and right children to the root
# print("left position addition ")
# left_position = tree.add_left(root_position, 2)
#right_position = tree.add_right(root_position, 3)

# Add children to the left node
#left_left_position = tree.add_left(left_position, 4)
#left_right_position = tree.add_right(left_position, 5)

# Add children to the right node
#right_left_position = tree.add_left(right_position, 6)
#right_right_position = tree.add_right(right_position, 7)
#tree.display_tree()


