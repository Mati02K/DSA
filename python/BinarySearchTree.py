import collections

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
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

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

    # Iterative ways of preorder,inorder and postorder

def pre_order_traversal_iterative(tree):
    elements = []
    if not tree:
        return elements
    stack = [tree]
    while stack:
        tree = stack.pop()
        elements.append(tree.data)
        if tree.right:
            stack.append(tree.right)
        if tree.left:
            stack.append(tree.left)
    return elements

def in_order_traversal_iterative(tree):
    elements = []
    if not tree:
        return elements
    stack = []
    while tree is not None or stack != []:
        while tree is not None:
            stack.append(tree)
            tree = tree.left
        tree = stack.pop()
        elements.append(tree.data)
        tree = tree.right

    return elements

def post_order_traversal_iterative(tree):
    postorder = []
    if not tree:
        return postorder
    stack = [tree]
    while stack:
        curr = stack.pop()
        postorder.append(curr.data)
        if (curr.left):
            stack.append(curr.left)
        if (curr.right):
            stack.append(curr.right)
    return postorder[::-1]

# Level order Traversal of a tree
# This is a BFS Approach where we we return elements in pair of levels
def level_Order_Traversal(root):
    result = []
    if not root:
        return result
    queue = collections.deque()
    queue.append(root)

    while queue:
        qlen = len(queue)
        level = []
        for i in range(qlen):
            node = queue.popleft()
            if node:
                level.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            result.append(level)

    return result

#Maximum depth of a tree (DFS)
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left),maxDepth(root.right))

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
    # print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    # print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
    # print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    # print("Minimum in the list:",numbers_tree.find_min())
    # print(numbers_tree.calculate_sum())
    print(pre_order_traversal_iterative(numbers_tree))
    print(in_order_traversal_iterative(numbers_tree))
    print(post_order_traversal_iterative(numbers_tree))
    print(level_Order_Traversal(numbers_tree))
    print(maxDepth(numbers_tree))
