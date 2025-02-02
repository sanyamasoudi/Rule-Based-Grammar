class TreeNode:
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
