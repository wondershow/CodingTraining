class DoubleLinkedNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = self.right = None

class LRUCache:
    "Tail in, head out"
    def __init__(self, capacity: int):
        self.size, self.cap = 0, capacity
        self.head = self.tail = DoubleLinkedNode(0, 0)
        self.head.right = self.tail
        self.tail.left = self.head
        self.nodes = {}

    def _remove_linked_node(self, node):
        left, right = node.left, node.right
        left.right = right
        right.left = left
        del self.nodes[node.key]
        self.size -= 1
    
    # insert a node to the right of a node
    def _insert_after(self, left_node, node):
        old_right = left_node.right
        left_node.right = old_right.left = node
        node.left, node.right = left_node, old_right
        self.nodes[node.key] = node
        self.size += 1
        if self.size > self.cap:
            self._evict()
        
    
    def _add_tail(self, node):
        self._insert_after(self.tail.left, node)
        
    def _evict(self):
        self._remove_linked_node(self.head.right)
    
    
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._remove_linked_node(node)
        self._add_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            node = DoubleLinkedNode(key, value)
            self._add_tail(node)
        else:
            node = self.nodes[key]
            node.val = value
            self._remove_linked_node(node)
            self._add_tail(node)
