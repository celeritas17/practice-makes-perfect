# 1.6
def rotate(A, length):
	layers = length//2

	for i in range(layers):
		'''
		# top left to top right
		temp = A[i][j]
		A[i][j] = A[i][i]
		
		# bottom left to top left
		A[i][i] = A[j][i]

		# bottom right to bottom left
		A[j][i] = A[j][j]

		# top right to bottom right
		A[j][j] = temp


		[3, 4, 5, 6, . , . , . ] [1, 2, 3]

		[7, . , . , . ] [1, 2, 3]
		'''

# 11.1
def merge_into_A(A, B, cut_point):
	lastA = cut_point - 1
	lastB = len(B) - 1
	lastIndex = cut_point + len(B) - 1

	indexA = lastA
	indexB = lastB

	while indexA >= 0 and indexB >= 0:
		if A[indexA] > B[indexB]:
			A[lastIndex] = A[indexA]
			indexA -= 1
		else:
			A[lastIndex] = B[indexB]
			indexB -= 1
		lastIndex -= 1

	while indexB >= 0:
		A[lastIndex] = B[indexB]
		indexB -= 1
		lastIndex -= 1


if __name__ == '__main__':
	A = []
	B = []
	merge_into_A(A, B, 0)
	print(A)


	#A = [[1, 2], [3, 4]]
	#B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	#rotate(B, 3)
	#print(B)