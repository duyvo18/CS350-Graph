test_cases = int(input())

for _ in range(test_cases):
    boy_count, girl_count, couple_count = map(int, input().split())
    
    boy_deg = [0] * (boy_count + 1)
    girl_deg = [0] * (girl_count + 1)
    
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    
    for i in boys:
        boy_deg[i] += 1
    
    for i in girls:
        girl_deg[i] += 1
        
    ans = 0
    for i in range(couple_count):
        ans += couple_count - boy_deg[boys[i]] - girl_deg[girls[i]] + 1
    
    print(ans//2)