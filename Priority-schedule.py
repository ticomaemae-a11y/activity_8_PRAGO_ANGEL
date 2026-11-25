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


# Activity 6: Priority Scheduler
def priority_scheduler(jobs):
    priority_queue = Heap(is_min=False)

    for priority, job_name in jobs:
        priority_queue.insert((priority, job_name))

    release_order = []

    while priority_queue.size() > 0:
        priority, job_name = priority_queue.extract()
        release_order.append(job_name)

        print("Released:", job_name, "| Priority:", priority)

    return release_order


jobs = [
    (2, "Job A"),
    (5, "Job B"),
    (1, "Job C"),
    (4, "Job D")
]

order = priority_scheduler(jobs)

print("Release order:", order)