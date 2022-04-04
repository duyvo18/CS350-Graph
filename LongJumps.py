loop = int(input())

for _ in range(loop):
    n = int(input())
    jumpDist = list(map(int,input().split()))
    for idx in range(n-1, -1, -1):
        if idx + jumpDist[idx] < n:
            jumpDist[idx] += jumpDist[idx + jumpDist[idx]]
    print(max(jumpDist))