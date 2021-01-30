from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k, self.heap = k, []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # 以小为大，以体为用
        # 规模为k的小顶堆，其堆顶即为第k大元素
        # if len(self.heap) < self.k:
        #     heappush(self.heap, val)
        # elif self.heap[0] < val:
        #     heappop(self.heap)
        #     heappush(self.heap, val)
        # return self.heap[0]

        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]

# def heapify(heap: list):
#     for i in reversed(range(len(heap) // 2)):
#         _shift_down(heap, i)


def heappush(heap: List, num: int):
    heap.append(num)
    _shift_up(heap, len(heap) - 1)


def heappop(heap: List) -> int:
    heap[0], heap[-1] = heap[-1], heap[0]
    top = heap.pop()
    if len(heap) > 0:
        _shift_down(heap, 0)
    return top

def _shift_up(heap: List, i: int):
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        parent = (i - 1) // 2
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent


def _shift_down(heap: List, i: int):
    while i < len(heap) // 2:
        il, ir = 2 * i + 1, 2 * i + 2
        _min = i
        if il < len(heap) and heap[_min] > heap[il]:
            _min = il
        if ir < len(heap) and heap[_min] > heap[ir]:
            _min = ir
        if i == _min:
            break
        heap[i], heap[_min] = heap[_min], heap[i]
        i = _min


if __name__ == '__main__':
    a = [4, 1, 5, 2, 3, 7]
    s = KthLargest(3, [])
    for x in a:
        print(s.add(x))



