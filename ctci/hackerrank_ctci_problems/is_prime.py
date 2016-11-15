def is_prime(n):
    # assume n >= 1
    if n == 1: return False
    if n == 2: return True
    if n%2 == 0: return False
    
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    
    return True
        

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if is_prime(n):
        print('Prime')
    else:
        print('Not prime')
        