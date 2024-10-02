class TreeNode:
    def __init__(self, key, value):
        self.key = key  
        self.value = value  
        self.left = None  
        self.right = None  

class BinaryTree:
    def __init__(self):
        self.root = None

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current 
       
    def _insert(self, current_node, new_node):
        if new_node.key < current_node.key:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(current_node.right, new_node)

    def insert(self, key, value):
        new_node = TreeNode(key, value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _search(self, current_node, key):
            if current_node is None or current_node.key == key:
                return current_node
            if key < current_node.key:
                return self._search(current_node.left, key)
            else:
                return self._search(current_node.right, key)  
              
    def search(self, key):
        return self._search(self.root, key)
    
    def _delete(self, current_node, key):
        if current_node is None:
            return current_node
        
        if key < current_node.key:
            current_node.left = self._delete(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self._delete(current_node.right, key)
        else:
            
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            
            min_larger_node = self._get_min(current_node.right)
            current_node.key = min_larger_node.key
            current_node.value = min_larger_node.value
            current_node.right = self._delete(current_node.right, min_larger_node.key)
        
        return current_node 
       
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _inorder_traversal(self, current_node, elements):
        if current_node is not None:
            self._inorder_traversal(current_node.left, elements)
            elements.append((current_node.key, current_node.value))
            self._inorder_traversal(current_node.right, elements)
      
    def inorder_traversal(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        return elements
    
