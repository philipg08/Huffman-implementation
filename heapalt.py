class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, node):
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_up(self, index):
        parent_index = (index - 1) // 2

        while index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_index = index

        if (
            left_child_index < len(self.heap) and
            self.heap[left_child_index] < self.heap[smallest_index]
        ):
            smallest_index = left_child_index

        if (
            right_child_index < len(self.heap) and
            self.heap[right_child_index] < self.heap[smallest_index]
        ):
            smallest_index = right_child_index

        if smallest_index != index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self.heapify_down(smallest_index)