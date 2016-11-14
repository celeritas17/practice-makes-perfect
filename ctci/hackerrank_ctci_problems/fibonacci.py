import functools

def fib(n, computed={0:0, 1:1}):
	if n not in computed:
		computed[n] = fib(n - 1, computed) + fib(n - 2, computed)
	return computed[n]

# (!) (!) (!) Interesting. 
@functools.lru_cache(None)
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
        
n = 39
print(fib(n))