def davis(n, computed={0:1, 1:1, 2:2}):
    if n not in computed:
        computed[n] = davis(n - 1, computed) + davis(n - 2, computed) + davis(n - 3, computed) 
    return computed[n]

s = int(input().strip())
for _ in range(s):
    n = int(input().strip())
    print(davis(n))