from Node import Node


class Tree:

    def __init__(self, data):
        self.root = Node(data)

    def add_node(self, parent_node_data, new_node):
        target_node = self.__find_node(self.root, parent_node_data)
        target_node.children.append(new_node)
        return
    
    def remove_node(self, data):
        target_node = self.__find_node_parent(self.root, data)
        for i, child in enumerate(target_node.children):
            if child.data == data:
                target_node.children.pop(i)
        return


    def __find_node(self, node, data):
        if node.data == data:
            return node
        if len(node.children) == 0:
            return None
        for child in node.children:
            target = self.__find_node(child, data)
            if target is not None:
                return target
        return None
    
    def __find_node_parent(self, node, data):
        if len(node.children) == 0:
            return None
        for child in node.children:
            if child.data == data:
                return node
        for child in node.children:
            target = self.__find_node_parent(child, data)
            if target is not None:
                return target
        return None