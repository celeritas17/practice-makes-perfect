def merge_bad(arr1, arr2):
	merged = []

	i = j = 0

	while i < len(arr1) or j < len(arr2):
		if i == len(arr1):
			merged.append(arr2[j])
			j += 1
		elif j == len(arr2):
			merged.append(arr1[i])
			i += 1
		elif arr1[i] <= arr2[j]:
			merged.append(arr1[i])
			i += 1
		else:
			merged.append(arr2[j])
			j += 1

	return merged

def merge_sort_bad(arr):
	if not arr or len(arr) <= 1:
		return arr

	return merge(merge_sort(arr[0:len(arr)//2]), merge_sort(arr[len(arr)//2:]))

def merge(arr, start, end, mid):
	i = 0
	j = 0

	left = arr[start:mid]
	right = arr[mid:end]

	for k in range(start, end):
		if i == len(left):
			arr[k] = right[j]
			j += 1
		elif j == len(right):
			arr[k] = left[i]
			i += 1
		elif left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1

def merge_sort(arr, start, end):
	if (end - start) > 1:
		merge_sort(arr, start, (start + end)//2)
		merge_sort(arr, (start + end)//2, end)
		merge(arr, start, end, (start + end)//2)

if __name__ == '__main__':
	a = [3, 2, 1, 7, 13, 10, 9, 8]
	merge_sort(a, 0, len(a))
	print(a)