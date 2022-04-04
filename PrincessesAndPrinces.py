test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    
    unmarried_prince = [True] * n
    unmarried_princess = 0
    
    for princess_idx in range(n):
        prince_matches = list(map(int, input().split()))[1:]
        unmarried = True
        
        
        for idx in prince_matches:
            if unmarried_prince[idx - 1]:
                unmarried_prince[idx - 1] = False
                unmarried = False
                break
        
        if unmarried:
            unmarried_princess = princess_idx + 1
    
    if unmarried_princess:
        print("IMPROVE")
        print(f"{unmarried_princess} {unmarried_prince.index(True) + 1}")
    else:
        print("OPTIMAL")