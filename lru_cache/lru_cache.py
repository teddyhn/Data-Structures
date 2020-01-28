from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max_nodes = limit
        self.current_nodes = 0
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            current_node = self.cache.head
            
            while True:
                if current_node.value == key:
                    self.cache.move_to_end(current_node)
                    break
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    break
            return self.storage[key]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if self.current_nodes >= self.max_nodes and key not in self.storage:
            head = self.cache.remove_from_head()
            self.storage.pop(head)

        if key not in self.storage:
            self.current_nodes += 1
        self.storage[key] = value
        self.cache.add_to_tail(key)



