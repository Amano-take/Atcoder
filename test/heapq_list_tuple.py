import random
import heapq
import time

"""
なぜかheapq.heappopはtupleのほうが早い。結果は同じ
"""

N = 1000000
test_tuple_A = []
for _ in range(N):
    a = int(random.random() * 10**6)
    b = int(random.random() * 10**6)
    test_tuple_A.append((a, b))
test_tuple_B = []
for _ in range(N):
    a = int(random.random() * 10**6)
    b = int(random.random() * 10**6)
    test_tuple_B.append((a, b))
test_list_A = list(map(list, test_tuple_A))
test_list_B = list(map(list, test_tuple_B))

start = time.time()
heapq.heapify(test_tuple_A)
end = time.time()
print(end - start, end=":")
print("heapify tuple")

start = time.time()
heapq.heapify(test_list_A)
end = time.time()
print(end - start, end=":")
print("heapify list")

start = time.time()
for i in range(N):
    heapq.heappush(test_tuple_A, test_tuple_B[i])
for i in range(N):
    heapq.heappop(test_tuple_A)
end = time.time()
print(end - start, end=":")
print("heap tuple")

start = time.time()
for i in range(N):
    heapq.heappush(test_list_A, test_list_B[i])
for i in range(N):
    heapq.heappop(test_list_A)
end = time.time()
print(end - start, end=":")
print("heap list")