from heapq import heappush, heappop

n = int(input().strip())
a = float(input().strip())
print(a)
b = float(input().strip())
print((a + b)/2)
# assuming positive numbers!

high_heap = []
low_heap = []

heappush(high_heap, max(a, b))
heappush(low_heap, -min(a, b))

count = 2
while count < n:
    a = float(input().strip())
    max_low = -low_heap[0]
    min_high = high_heap[0]
    
    if a <= max_low:
        heappush(low_heap, -a)
    else:
        heappush(high_heap, a)
    
    if abs(len(high_heap) - len(low_heap)) > 1:
        if len(high_heap) > len(low_heap):
            num = heappop(high_heap)
            heappush(low_heap, -num)
        else:
            num = -heappop(low_heap)
            heappush(high_heap, num)
    
    if  len(high_heap) > len(low_heap):
        median = high_heap[0]
    elif len(high_heap) < len(low_heap):
        median = -low_heap[0]
    else:
        median = (high_heap[0] - low_heap[0])/2
        
    print(median)
    count += 1