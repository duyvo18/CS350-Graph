INF = float("inf")

employee_count = int(input())
input()
application_count = int(input())

supervise_cost = [INF for _ in range(employee_count + 1)]

for application in range(application_count):
    employee, cost = map(int, input().split()[1:])
    
    if cost < supervise_cost[employee]:
        supervise_cost[employee] = cost

supervise_cost = supervise_cost[1:]       
supervise_cost.remove(INF);

if INF in supervise_cost:
    print(-1)
else:
    print(sum(supervise_cost))