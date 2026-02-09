class Task:
    def __init__(self, task_id, priority, arrival_time=0):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time


class MaxHeapPriorityQueue:
    def __init__(self):
        self.heap = []
        self.pos = {}  # task_id -> index

    def is_empty(self):
        return len(self.heap) == 0

    # ---------- helper methods ----------
    def _parent(self, i):
        return (i - 1) // 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos[self.heap[i].task_id] = i
        self.pos[self.heap[j].task_id] = j

    def _sift_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self.heap[i].priority > self.heap[p].priority:
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            if left >= n:
                break

            right = left + 1
            best = left
            if right < n and self.heap[right].priority > self.heap[left].priority:
                best = right

            if self.heap[best].priority > self.heap[i].priority:
                self._swap(i, best)
                i = best
            else:
                break

    # ---------- required operations ----------
    def insert(self, task):
        if task.task_id in self.pos:
            raise ValueError("task_id already exists")

        self.heap.append(task)
        idx = len(self.heap) - 1
        self.pos[task.task_id] = idx
        self._sift_up(idx)

    def extract_max(self):
        if self.is_empty():
            raise IndexError("extract_max from empty priority queue")

        top = self.heap[0]
        last = self.heap.pop()
        del self.pos[top.task_id]

        if not self.is_empty():
            self.heap[0] = last
            self.pos[last.task_id] = 0
            self._sift_down(0)

        return top

    def increase_key(self, task_id, new_priority):
        if task_id not in self.pos:
            raise KeyError("task_id not found")

        i = self.pos[task_id]
        if new_priority < self.heap[i].priority:
            raise ValueError("new_priority is smaller; use decrease_key")

        self.heap[i].priority = new_priority
        self._sift_up(i)

    def decrease_key(self, task_id, new_priority):
        if task_id not in self.pos:
            raise KeyError("task_id not found")

        i = self.pos[task_id]
        if new_priority > self.heap[i].priority:
            raise ValueError("new_priority is larger; use increase_key")

        self.heap[i].priority = new_priority
        self._sift_down(i)


# ---------- test code ----------
if __name__ == "__main__":
    pq = MaxHeapPriorityQueue()

    pq.insert(Task("A", 10))
    pq.insert(Task("B", 5))
    pq.insert(Task("C", 1))

    pq.decrease_key("A", 2)

    print("top:", pq.heap[0].task_id, pq.heap[0].priority)  # B 5
