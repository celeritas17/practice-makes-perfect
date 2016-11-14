from heapq import heappush, heappop

def heapsort(arr):
	arr_sorted = []
	heap = []
	for n in arr:
		heappush(heap, n)

	while heap:
		arr_sorted.append(heappop(heap))

	return arr_sorted


if __name__ == '__main__':
	data = [7, 1, 3, 2, 4, 5, 9, 8, 100, 16, 50]
	print('data: ', data)
	data_sorted = heapsort(data)
	print('data_sorted: ', data_sorted)
	data.sort()
	print('data_sorted == data.sort(): ', data_sorted == data)