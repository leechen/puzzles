
public class Node {
    public int key, val;
    public Node prev, next;
    
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

public class LRUCache {
    private int capacity;
    private Dictionary<int, Node> cache;
    private Node left, right;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new Dictionary<int, Node>();

        left = new Node(0, 0);
        right = new Node(0, 0);
        left.next = right;
        right.prev = left;
    }

    private void Remove(Node node) {
        Node prev = node.prev, next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    private void Insert(Node node) {
        Node prev = right.prev, next = right;
        prev.next = node;
        next.prev = node;
        node.prev = prev;
        node.next = next;
    }

    public int Get(int key) {
        if (cache.ContainsKey(key)) {
            Node node = cache[key];
            Remove(node);
            Insert(node);
            return node.val;
        }
        return -1;
    }

    public void Put(int key, int value) {
        if (cache.ContainsKey(key)) {
            Remove(cache[key]);
        }
        cache[key] = new Node(key, value);
        Insert(cache[key]);

        if (cache.Count > capacity) {
            Node lru = left.next;
            Remove(lru);
            cache.Remove(lru.key);
        }
    }
}
