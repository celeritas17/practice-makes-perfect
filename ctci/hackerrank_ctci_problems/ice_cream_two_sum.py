t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = [int(x) for x in input().strip().split(' ')]
    cost_map = {}
    
    for index, cost in enumerate(a):
        if (m - cost) in cost_map:
            print('{0:d} {1:d}'.format(cost_map[m - cost] + 1, index + 1))
            break
        else:
            cost_map[cost] = index