from random import randint

with open('nums.txt', 'r') as nums:
	numbers = nums.readlines()

numbers = [int(n.rstrip()) for n in numbers]

def choose_pivot(A, l , r):
	return randint(l, r - 1)

def partition(A, l, r):
	i = j = l + 1
	p = A[l]
	while j < r:
		if A[j] < p:
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
			i += 1
		j += 1

	# put the pivot where it belongs
	temp = A[i - 1]
	A[i - 1] = A[l]
	A[l] = temp

	return i - 1 # return location of boundary in partitioned array

def quicksort(A, l, r):
	if r - l <= 1:
		return

	p = choose_pivot(A, l, r)
	temp = A[l]
	A[l] = A[p]
	A[p] = temp

	boundary = partition(A, l, r)

	quicksort(A, l, boundary)
	quicksort(A, boundary + 1, r)

def quicksort_comparisons(A, l, r):
	if r - l <= 1:
		return 0

	c = r - l - 1
	p = choose_pivot(A, l, r)
	temp = A[l]
	A[l] = A[p]
	A[p] = temp

	boundary = partition(A, l, r)

	c += quicksort_comparisons(A, l, boundary)
	c += quicksort_comparisons(A, boundary + 1, r)

	return c

if __name__ == '__main__':
	print('quicksort!')
	A = [9, 7, 2, 1, 3, 14, 4, 27, 5]
	print(A)
	quicksort(A, 0, len(A))
	print(A)

	print('Week 2 assignment comparisons for list of 10000 integers: ', quicksort_comparisons(numbers, 0, len(numbers)))
