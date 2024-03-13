class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.map = {}
        self.cache = deque()

    def get(self, key: int) -> int:
        if key in self.map:
            self.cache.remove(key)
            self.cache.append(key)
            value = self.map[key]
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.c == len(self.cache):
                oldest = self.cache.popleft()
                del self.map[oldest]
        else:
            self.cache.remove(key)
        self.cache.append(key)
        self.map[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)