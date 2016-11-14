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
def median_sum(nums):
	pass


if __name__ == '__main__':
	#nums = load_nums(SUM_FILE)
	#print(two_sums_count(nums, -10000, 10000)) # 427

	nums = load_nums(MEDIAN_FILE)
	print(nums[len(nums) - 1])
