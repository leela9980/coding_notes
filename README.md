# python_notes
Python coding Interview quick tips

```python
Import heapq
heap = []
# min heap
heapq.heappush(heap, item)
heapq.heappop(heap)
heap[0] //top

# max heap (no max heap in python so we have to negate the value before inserting)
 heapq.heappush(heap, -item)
-heapq.heappop(heap)
-heap[0]
```



