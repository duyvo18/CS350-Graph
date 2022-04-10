V, max_cat = map(int, input().split())
cat_V = list(map(int, input().split()))
adj_list = {i: [] for i in range(1, V + 1)}

for i in range(V - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# Tuple of (next_vertex, cur_cat, cur_vertex)
queue = [(1, 0, 0)]
ans = 0

while queue:
    next_vertex, cur_cat, cur_vertex = queue.pop()
    cur_cat = (cur_cat + 1) * cat_V[next_vertex - 1]

    if cur_cat > max_cat:
        continue
    elif len(adj_list[next_vertex]) == 1 and next_vertex != 1:
        ans += 1
        continue
    else:
        for i in adj_list[next_vertex]:
            if i != cur_vertex:
                queue.append([i, cur_cat, next_vertex])

print(ans)
