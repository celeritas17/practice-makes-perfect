from random import randint

def choose_pivot(left, right):
	return randint(left, right - 1)

def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

def partition(A, left, right):
	pivot = A[left]
	i = j = left + 1

	while j < right:
		if A[j] < pivot:
			swap(A, i, j)
			i += 1
		j += 1

	swap(A, left, i - 1)
	return i - 1

def quickselect(A, left, right, index):
	if right - left <= 1:
		return A[left]

	p = choose_pivot(left, right)
	swap(A, left, p)
	boundary = partition(A, left, right)

	if boundary + 1 == index:
		return nums[boundary]

	if boundary + 1 > index:
		return quickselect(A, left, boundary, index)

	return quickselect(A, boundary + 1, right, index)

if __name__ == '__main__':
	nums = [4, 8, 6, 1, 3, 5, 9, 2]
	num = quickselect(nums, 0, len(nums), 8)
	print(num)
