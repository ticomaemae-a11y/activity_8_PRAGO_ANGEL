class Heap:
    def __init__(self, is_min=True):
        self.heap = []
        self.is_min = is_min

    def size(self):
        return len(self.heap)

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent], self.heap[index]
                )
                index = parent
            else:
                break

    def extract(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)

        return root

    def _sift_down(self, index):
        size = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest], self.heap[index]
            )
            index = smallest


def kth_largest(numbers, k):
    if k < 1 or k > len(numbers):
        return None

    min_heap = Heap(is_min=True)

    for number in numbers:
        min_heap.insert(number)

        if min_heap.size() > k:
            min_heap.extract()

    return min_heap.peek()


numbers = [3, 2, 1, 5, 6, 4]
k = 2

answer = kth_largest(numbers, k)
verified = sorted(numbers, reverse=True)[k - 1]

print("Kth largest:", answer)
print("Verified by sorting:", verified)