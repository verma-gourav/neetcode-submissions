class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        if key is not None and value is not None:
            self.map[key] = value

    def get(self, key: int) -> int:
        if key is not None:
            return self.map[key]
        return -1

    def remove(self, key: int) -> None:
        if key is not None:
            self.map[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)