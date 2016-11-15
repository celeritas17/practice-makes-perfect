'''
Given an array arr of n unique non-negative integers, 
how can you most efficiently find a non-negative integer 
that is not in the array?

Your solution should return such an integer or null if arr contains all possible integers.
Analyze the runtime and space complexity of your solution.
'''

MAX_INT = 10000000 # for instance

def different_number(arr):
	# numbers are distinct and non-negative,
	# So can't be a number missing if the array
	# has MAX_INT + 1 things (0..MAX_INT) 
	if len(arr) == MAX_INT + 1:
		return None

	int_map = {}

	for n in arr:
		int_map[n] = True

	# guaranteed to stop for some number between 0 and MAX_INT, inclusive
	i = 0
	while i <= MAX_INT and i in int_map:
		i += 1

	return i


if __name__ == '__main__':
	a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 100, 19292]
	print(different_number(a)) # 9
