class Heap:
    def __init__(self, is_min=True):
        self.heap = []
        self.is_min = is_min

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.size() == 0:
            return None
        return self.heap[0]

    def _higher_priority(self, a, b):
        if self.is_min:
            return a < b
        return a > b

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(self.size() - 1)

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

    def extract(self):
        if self.size() == 0:
            return None

        if self.size() == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)

        return root

    def _sift_down(self, index):
        size = self.size()

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

print("\nACTIVITY 1: MIN-HEAP")

numbers = [5, 9, 11, 14, 19, 17, 18, 13]

min_heap = Heap(is_min=True)

for number in numbers:
    min_heap.insert(number)

print("Peek:", min_heap.peek())
print("Size:", min_heap.size())

result = []

while min_heap.size() > 0:
    result.append(min_heap.extract())

print("Extract order:", result)

print("\nACTIVITY 2: MAX-HEAP")

numbers = [5, 9, 11, 14, 19, 17, 18, 13]

max_heap = Heap(is_min=False)

for number in numbers:
    max_heap.insert(number)

result = []

while max_heap.size() > 0:
    result.append(max_heap.extract())

print("Extract order:", result)

print("\nACTIVITY 3: HEAP SORT")


def heap_sort(array):
    max_heap = Heap(is_min=False)

    for number in array:
        max_heap.insert(number)

    result = []

    while max_heap.size() > 0:
        result.append(max_heap.extract())

    result.reverse()
    return result


print(heap_sort([4, 10, 3, 5, 1]))
print(heap_sort([1, 2, 3, 4, 5]))
print(heap_sort([5, 4, 3, 2, 1]))
print(heap_sort([4, 2, 4, 1, 2]))
print(heap_sort([]))

print("\nACTIVITY 4: KTH LARGEST")


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

print("\nACTIVITY 5: MERGE K SORTED ARRAYS")


def merge_k_sorted_arrays(arrays):
    min_heap = Heap(is_min=True)
    result = []

    # Insert the first value from each non-empty array
    for source in range(len(arrays)):
        if arrays[source]:
            min_heap.insert(
                (arrays[source][0], source, 0)
            )

    while min_heap.size() > 0:
        value, source, position = min_heap.extract()
        result.append(value)

        next_position = position + 1

        if next_position < len(arrays[source]):
            next_value = arrays[source][next_position]

            min_heap.insert(
                (next_value, source, next_position)
            )

    return result


arrays = [
    [1, 4, 7],
    [2, 5],
    [3, 6, 8, 9]
]

merged = merge_k_sorted_arrays(arrays)

print("Merged:", merged)
print("Is sorted:", merged == sorted(merged))

print("\nACTIVITY 6: PRIORITY SCHEDULER")


def priority_scheduler(jobs):
    priority_queue = Heap(is_min=False)

    for priority, job_name in jobs:
        priority_queue.insert((priority, job_name))

    release_order = []

    while priority_queue.size() > 0:
        priority, job_name = priority_queue.extract()
        release_order.append(job_name)

        print(
            "Released:", job_name,
            "| Priority:", priority
        )

    return release_order


jobs = [
    (2, "Job A"),
    (5, "Job B"),
    (1, "Job C"),
    (4, "Job D")
]

order = priority_scheduler(jobs)

print("Release order:", order)