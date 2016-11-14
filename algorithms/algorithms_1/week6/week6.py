from heapq import heappush, heappop

SUM_FILE = '2sum.txt'
MEDIAN_FILE = 'median.txt'

def load_nums(file):
	nums = []
	with open(file, 'r') as f:
		for line in f:
			nums.append(int(line.strip()))
	
	return nums

'''
Returns the number of distinct pairs of numbers
x, y in nums such that x + y is in the interval
[low, high]
'''
def two_sums_count(nums, low, high):
	nums_dict = {}
	sums = {}

	for n in nums:
		nums_dict[n] = True

	for t in range(low, high + 1):
		if t%1000 == 0:
			print(t)
		for n in nums:
			if t - n in nums_dict:
				sums[t] = True

	return len(sums)

'''
Return the sum of the len(nums) medians mod 10000
'''
def median_stream_sum(nums):
	median_sum = nums[0] + nums[1]
	high_heap = []
	low_heap = []
	count = 2

	# initialize high and low heaps
	heappush(high_heap, max(nums[0], nums[1]))
	heappush(low_heap, -min(nums[0], nums[1]))

	while count < len(nums):
		max_low = -low_heap[0]
		min_high = high_heap[0]

		a = nums[count]

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

		if len(low_heap) > len(high_heap):
			median = -low_heap[0]
		if len(high_heap) > len(low_heap):
			median = high_heap[0]
		else:
			median = -low_heap[0]

		median_sum += median

		count += 1
	
	return median_sum%10000

if __name__ == '__main__':
	#nums = load_nums(SUM_FILE)
	#print(two_sums_count(nums, -10000, 10000)) # 427

	nums = load_nums(MEDIAN_FILE)
	print(median_stream_sum(nums))
