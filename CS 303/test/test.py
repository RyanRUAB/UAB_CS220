import heapq

customers = [(2, "Harry"), (3, "Charles"), (1, "Riya"), (4, "Stacy")]
"""
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
"""
heapq.heapify(customers)


while customers:
     print(heapq.heappop(customers))