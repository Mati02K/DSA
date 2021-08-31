class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_min()


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.data== None:
            return
        else:
            if self.left:
                elements.append(self.left.post_order_traversal())
            if self.right:
                elements.append(self.right.post_order_traversal())
            elements.append(self.data)
        
        return elements

    def calculate_sum(self):
        total = 0
        if self.data==None:
            return total
        total = total + self.data
        if self.left:
            total = total + self.left.calculate_sum()
        if self.right:
            total = total + self.right.calculate_sum()
        
        return total


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(0,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([1,17, 4, 19, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
    print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    print("Minimum in the list:",numbers_tree.find_min())
    print(numbers_tree.calculate_sum())
