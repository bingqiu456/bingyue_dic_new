from typing import List

class Node:
    def __init__(self) -> None:
        self.children = dict()
        self.is_end = False

class DataTree:

    def __init__(self):
        self.root = Node()

    def add(self, uid: str) -> None:
        current_node = self.root
        for char in uid:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.is_end = True

    def search(self, uid: str) -> bool:
        current_node = self.root
        for char in uid:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end

    def add_list(self, uid:List[str]) -> None:
        for i in uid:
            self.add(i)

