class BinarySearchTreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self, value):
        if value == self.value:
            return
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTreeNode(value)
            else:
                self.left.add_child(value)
        if value > self.value:
            if self.right == None:
                self.right = BinarySearchTreeNode(value)
            else:
                self.right.add_child(value)
    
    def list_elements(self):
        elements = []
        if self.left:
            elements += self.left.list_elements()
        
        elements.append(self.value)

        if self.right:
            elements += self.right.list_elements()

        return elements

    def search(self, value):
        if self.value == value:
            return True
        if self.value < value:
            if self.right:
                return self.right.search(value)
        if self.value > value:
            if self.left:
                return self.left.search(value)
        return False

    def find_max(self):
        if self.right == None:
            return self.value
        else: 
            return self.right.find_max()

    def find_min(self):
        if self.left == None:
            return self.value
        else: 
            return self.left.find_min()
    
    def delete(self, value):
        if self.value == value:
            if self.right == None and self.left == None:
                return None
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right

            min_value = self.right.find_min()
            self.value = min_value
            self.right = self.right.delete(min_value)
        if self.value < value:
            if self.right:
                self.right = self.right.delete(value)
        if self.value > value:
            if self.left:
                self.left = self.left.delete(value)

        return self 


def build_tree_from_list(l1):
    root = BinarySearchTreeNode(l1[0])
    for i in range(1, len(l1)):
        root.add_child(l1[i])
    return root

#root = BinarySearchTreeNode(10)
#root.add_child(9)
#root.add_child(12)
l1 = [7,7,5,3,6,8,9,2,1,3,10,5,4]
root = build_tree_from_list(l1)
list1 = root.list_elements()