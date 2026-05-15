
class Node:
    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.children = dict()

    def add_child(self, child: "Node") -> bool:
        if not isinstance(child, Node):
            return False
        self.children[child.name] = child
        child.set_parent(self)
        return True
    
    def set_parent(self, parent: "Node") -> bool:
        if not isinstance(parent, Node):
            return False
        self.parent = parent
        return True
    
    def find_child(self, child_name: str) -> bool:
        if child_name in self.children.keys():
            return True
        return False