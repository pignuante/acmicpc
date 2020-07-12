num = int(input())
budgets = sorted(list(map(int, input().split())))
budget = int(input())

low = 1
high = budgets[-1]
result = 0
while high >= low:
    mid = (low+high) // 2  # 상한액
    t = sum([mid if i > mid else i for i in budgets])

    if budget >= t:
        low = mid + 1
        result = mid
    else:
        high = mid - 1

print(result)
