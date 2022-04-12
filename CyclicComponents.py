V, E = map(int, input().split())

adj_list = {i:[] for i in range(1, V + 1)}

for _ in range(E):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

candidates = set(i for i in range(1, V + 1) if len(adj_list[i]) == 2)

ans = 0
while candidates:
    v = candidates.pop()
    v_start, v_end = adj_list[v]
    
    while v_start in candidates:
        candidates.remove(v_start)
        
        v_start_next, v_start_next_prime = adj_list[v_start]
        
        if v_start_next in candidates:
            v_start = v_start_next
        elif v_start_next_prime in candidates:
            v_start = v_start_next_prime
        else:
            break
        
        if v_start == v_end:
            ans += 1

print(ans)