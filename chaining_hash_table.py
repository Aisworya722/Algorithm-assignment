class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of buckets (chains)

    def _hash(self, key):
        # simple hash: convert key to string, then use Python hash
        return hash(str(key)) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        # if key exists, update value
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # otherwise add new pair
        bucket.append((key, value))

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for (k, v) in bucket:
            if k == key:
                return v

        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True

        return False
