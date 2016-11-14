'''
Given an array of sorted distinct integers named arr, 
write a function that returns an index i in arr for which 
arr[i] = i or -1 if no such index exists.
'''

def arr_index_element_equality(arr, low, high):
	if low > high:
		return -1
	if (high - low) == 0:
		return low if arr[low] == low else -1

	median = (low + high)//2

	if arr[median] == median:
		return median

	if arr[median] > median:
		return arr_index_element_equality(arr, low, median)

	return arr_index_element_equality(arr, median, high)

if __name__ == '__main__':
	print(arr_index_element_equality([-2, -1, 2, 10, 11, 12, 100, 107, 188, 1999, 10000000], 0, 9)) # 2