class Heap:
    def __init__(self, is_min=True):
        self.heap = []
        self.is_min = is_min

    def size(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)

        return root

    def _higher_priority(self, a, b):
        if self.is_min:
            return a < b
        return a > b

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self._higher_priority(
                self.heap[index], self.heap[parent]
            ):
                self.heap[index], self.heap[parent] = (
                    self.heap[parent], self.heap[index]
                )
                index = parent
            else:
                break

    def _sift_down(self, index):
        size = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            best = index

            if left < size and self._higher_priority(
                self.heap[left], self.heap[best]
            ):
                best = left

            if right < size and self._higher_priority(
                self.heap[right], self.heap[best]
            ):
                best = right

            if best == index:
                break

            self.heap[index], self.heap[best] = (
                self.heap[best], self.heap[index]
            )
            index = best


# Activity 2: Max-heap
numbers = [5, 9, 11, 14, 19, 17, 18, 13]

max_heap = Heap(is_min=False)

for number in numbers:
    max_heap.insert(number)

result = []

while max_heap.size() > 0:
    result.append(max_heap.extract())

print("Extract order:", result)