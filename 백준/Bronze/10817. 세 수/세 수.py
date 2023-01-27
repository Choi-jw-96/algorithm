#10817
import heapq
A, B, C = map(int, input().split())
heap = []
heapq.heappush(heap, A)
heapq.heappush(heap, B)
heapq.heappush(heap, C)

heapq.heappop(heap)     # 제일 앞에 있는(최소값) 값을 지워라
print(heap[0])
