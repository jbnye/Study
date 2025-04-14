class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    #inserts
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insertNode(self.root, value)
    def _insertNode(self, current, value):
        if value < current.val:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insertNode(current.left, value)
        elif value > current.val:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insertNode(current.right, value)
        else:
            print(f"Value: {value} is already in the tree.")


    def search(self, value):
        if self.root is None:
            return ("There is not tree to search.")
        else:
            return self._search(self.root, value)
    def _search(self, current, value):
        if current is None:
            return False
        if value < current.val:
            return self._search(current.left, value)
        elif value > current.val:
            return self._search(current.right, value)
        else:
            return True



    def delete(self, value):
        if self.root is None:
            return ("There is not tree to delete a node")
        if self.search(value) is False:
            return("Value not in tree")
        else:
            self._delete(self.root, value)
    def _delete(self, current, value):
        if current is None:
            return
        if value < current.val:
            current.left = self._delete(current.left, value)
        elif value > current.val:
            current.right = self._delete(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.left is None:
                return current.left
            else:
                replacement = self._findLeft(current.right)
                current.val = replacement.val
                current.right = self._delete(current.right, replacement.val)
        return current          
    def _findLeft(self, node):
        while node.left is not None:
            node = node.left
        return node


    def preOrderTraversal(self):
        if self.root is None:
            return ("There is not tree to traverse.")
        else:
            self._preOrderTraversal(self.root)
    def _preOrderTraversal(self, current):
        if current is None:
            return
        else:
            print(current.val)
            self._preOrderTraversal(current.left)
            self._preOrderTraversal(current.right)


    def postOrderTraversal(self):
        if self.root is None:
            return ("There is not tree to traverse.")
        else:
            self._postOrderTraversal(self.root)
        
    def _postOrderTraversal(self, current):
        if current is None:
            return
        else:
            self._postOrderTraversal(current.left)
            print(current.val)
            self._postOrderTraversal(current.right)


    def inOrderTraversal(self):
        if self.root is None:
            return ("There is not tree to traverse.")
        else:
            self._inOrderTraversal(self.root)
    def _inOrderTraversal(self, current):
        if current is None:
            return
        else:
            self._inOrderTraversal(current.left)
            self._inOrderTraversal(current.right)
            print(current.val)

    
tree = BST()
array = [4, 2, 6, 1, 3, 5, 7]
for arr in array:
    tree.insert(arr)
tree.preOrderTraversal()
# tree.postOrderTraversal()
# tree.inOrderTraversal()
# print(tree.search(2))
# print(tree.search(8))
tree.delete(7)
tree.preOrderTraversal()
tree.delete(2)
tree.preOrderTraversal()


