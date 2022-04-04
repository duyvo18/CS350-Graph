_, dest = map(int, input().split())

portalArr = list(map(int, input().split()))

idx = 1
while idx < dest:
    idx += portalArr[idx - 1]

print("YES" if idx == dest else "NO")
