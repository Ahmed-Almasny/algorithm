class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, priority, name):
        self.heap.append((priority, name))
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] > self.heap[parent][0]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def extract_max(self):
        if not self.heap:
            return None
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            i = 0
            n = len(self.heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                if left < n and self.heap[left][0] > self.heap[largest][0]:
                    largest = left
                if right < n and self.heap[right][0] > self.heap[largest][0]:
                    largest = right
                if largest == i:
                    break
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
        return top

    def is_empty(self):
        return len(self.heap) == 0


scheduler = MaxHeap()

scheduler.insert(3, "Open browser")
scheduler.insert(10, "System update")
scheduler.insert(5, "Play music")
scheduler.insert(8, "Antivirus scan")

print("Running tasks by priority:")
while not scheduler.is_empty():
    priority, name = scheduler.extract_max()
    print(f"Priority {priority}: {name}")

scheduler.insert(7, "Print document")
scheduler.insert(9, "Backup files")

print("\nNew tasks:")
while not scheduler.is_empty():
    priority, name = scheduler.extract_max()
    print(f"Priority {priority}: {name}")
