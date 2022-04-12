from heapq import heappush, heappop

INF = float("inf")

V, E = map(int, input().split())

adi_list = {i:[] for i in range(1, V + 1)}
min_dist = [INF if i != 1 else 0 for i in range(V + 1)]
prev_V = [-1 for _ in range(V + 1)]

for i in range(1, E + 1):
    start, end, weight = map(int, input().split())
    adi_list[start] += [(weight, end)]
    adi_list[end] += [(weight, start)]
    
min_heap = [(0, 1)]

while min_heap:
    cur_cost, cur_V = heappop(min_heap)
    for edges in adi_list[cur_V]:
        next_V = edges[1]
        
        new_cost = cur_cost + edges[0]
        new_prev = cur_V
        
        if new_cost < min_dist[next_V]:
            prev_V[next_V] = cur_V
            min_dist[next_V] = new_cost
            
            heappush(min_heap, (new_cost, next_V))

if min_dist[V] == INF:
    print(-1)
else:
    path = []
    i = V
    while i != -1:
        path.append(i)
        i = prev_V[i]
        
    path.reverse()
    print(' '.join(map(str, path)))