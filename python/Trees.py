class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

class TreeDoubleNode(TreeNode):
    def __init__(self, data,key):
        self.data = data
        self.children = []
        self.key = key
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,key):
        if key == 'both':
            value = self.data + " (" + self.key + ")"
        elif key == 'name':
            value = self.data
        else:
            value = self.key
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(key)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeDoubleNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeDoubleNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeDoubleNode("Abhijit", "App Manager"))

    cto = TreeDoubleNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeDoubleNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeDoubleNode("Gels","HR Head")

    hr_head.add_child(TreeDoubleNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeDoubleNode("Waqas", "Policy Manager"))

    ceo = TreeDoubleNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    build_product_tree()
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")