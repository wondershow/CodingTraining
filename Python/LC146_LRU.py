class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size, self.cap = 0, capacity
        
        ##Add at tail, evict at head
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.right, self.tail.left = self.tail, self.head
        
        self.node_map = {}
        
    def _delete_node_dlist(self, node):
        left_node, right_node = node.left, node.right
        left_node.right, right_node.left = right_node, left_node
        
    def _insert_node_dlist(self, node):
        old_last = self.tail.left
        old_last.right = self.tail.left = node
        node.left, node.right = old_last, self.tail
    
    # key must exist
    def _remove_key_lru(self, key):
        node = self.node_map[key]
        self._delete_node_dlist(node)
        self.size -= 1
        del self.node_map[key]
    
    # key must not exist
    def _add_key_lru(self, key, val):
        node = Node(key, val)
        self._insert_node_dlist(node)
        self.node_map[key] = node
        self.size += 1

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        res = self.node_map[key].val
        self._remove_key_lru(key)
        self._add_key_lru(key, res)
        return res
        

    def put(self, key: int, value: int) -> None:
        if key not in self.node_map:
            self._add_key_lru(key, value)
        else:
            self._remove_key_lru(key)
            self._add_key_lru(key, value)
        if self.size > self.cap:
            self._remove_key_lru(self.head.right.key)



class LRUCache1:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity: int):
        # do intialization if necessary
        self.cap = capacity
        self.count = 0
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.right, self.tail.left = self.tail, self.head
        self.node_by_key = {}

    def _add_to_head(self, node):
        old_first = self.head.right
        self.head.right, node.left = node, self.head
        node.right, old_first.left = old_first, node
        self.node_by_key[node.key] = node
        self.count += 1
    
    def _remove_node(self, node):
        before, after = node.left, node.right
        before.right, after.left = after, before
        del self.node_by_key[node.key]
        self.count -= 1
    
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key: int) -> int:
        # write your code here
        if key not in self.node_by_key:
            return -1
        node = self.node_by_key[key]
        self._remove_node(node)
        self._add_to_head(node)
        return node.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def put(self, key: int, value: int) -> None:
        # write your code here
        if key in self.node_by_key:
            node = self.node_by_key[key]
            node.val = value
            self._remove_node(node)
        else:
            node = Node(key, value)
        self._add_to_head(node)
        if self.count > self.cap:
            self._remove_node(self.tail.left)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
