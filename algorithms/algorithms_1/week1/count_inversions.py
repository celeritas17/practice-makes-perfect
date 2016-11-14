#import urllib.request

#numbers = urllib.request.urlopen('https://d18ky98rnyall9.cloudfront.net/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt?Expires=1474502400&Signature=M3QWuKa48UbX-TxlKMa0IEgtL8AZEYjUhMGQQhq3JYuAudSPS9zLXinCjJP7oZB-ycHLSsfY8DjIhsMXvaGOzsNHUVvfIvBl~f0PcBe5VWZtCotnGi6OuzIQJSnQZyuYME3tx0-NNH1Fh2Bt-Mun3IN72QYtwsqNOfjryBNEDpk_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A').readlines()
#numbers = [int(n.rstrip()) for n in numbers]

from sorting import merge_sort

with open('nums.txt', 'r') as nums:
	numbers =  nums.readlines()

numbers = [int(n.rstrip()) for n in numbers]

def count_split_inversions(arr):
	if not arr or len(arr) <= 1:
		return 0
	
	length = len(arr)
	left = arr[0:length//2]
	right = arr[length//2:]

	right.sort()
	left.sort()

	left_index = 0
	right_index = 0
	left_len = len(left)
	right_len = len(right)
	num_inversions = 0

	while (left_index < left_len) and (right_index < right_len):
		if left[left_index] <= right[right_index]:
			left_index += 1
		else:
			num_inversions += (left_len - left_index)
			right_index += 1

	return num_inversions

def count_inversions(arr):
	if not arr or len(arr) <= 1:
		return 0
	length = len(arr)

	left = arr[0:length//2]
	right = arr[length//2:]

	return count_inversions(left) + count_inversions(right) + count_split_inversions(arr) 

if __name__ == '__main__':
	print(count_inversions(numbers))
