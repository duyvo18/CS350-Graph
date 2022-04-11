V, E = map(int, input().split())

adi_list = {i:[] for i in range(1, E + 1)}
for i in range(1, E + 1):
    start, end, weight = map(int, input().split())
    adi_list[start] += [(end, weight)]
    adi_list