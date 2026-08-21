class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Sentinel (dummy) nodes to avoid edge-case checks
        self.left = Node()   # left.next is Least Recently Used (LRU)
        self.right = Node()  # right.prev is Most Recently Used (MRU)
        self.left.next = self.right
        self.right.prev = self.left

    # Helper: remove an arbitrary node from the list
    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper: insert a node at the right (MRU position)
    def _insert(self, node: Node) -> None:
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # Move accessed node to MRU position
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node if key already exists
            self._remove(self.cache[key])

        # Create and insert new node as MRU
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)

        # Evict LRU node if capacity is exceeded
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self._remove(lru_node)
            del self.cache[lru_node.key]