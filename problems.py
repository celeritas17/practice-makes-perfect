# count the number of permutations of a in b
# assume len(a) <= len(b)
def count_permutations_in_string(a, b):
	permutations = 0
	a_char_counts = {}
	
	for char in a:
		if char in a_char_counts:
			a_char_counts[char] += 1
		else:
			a_char_counts[char] = 1

	for i in range(len(b)):
		index = i
		if b[index] in a_char_counts:
			match_count = 0
			a_perm_counts = {}
			still_going = True
			while still_going and match_count < len(a) and index < len(b):
				if b[index] in a_char_counts:
					if b[index] in a_perm_counts:
						a_perm_counts[b[index]] += 1
					else:
						a_perm_counts[b[index]] = 1

					if a_perm_counts[b[index]] <= a_char_counts[b[index]]:
						match_count += 1
						index += 1
					else:
						still_going = False
				else:
					still_going = False
			
			if match_count == len(a):
				permutations += 1

	return permutations

'''
Start with two arrays of strings, A and B, each with its elements in alphabetical order and without duplicates. 
Return a new array containing the first N elements from the two arrays. The result array should be in alphabetical 
order and without duplicates. A and B will both have a length which is N or more. The best "linear" solution makes 
a single pass over A and B, taking advantage of the fact that they are in alphabetical order, copying elements directly 
to the new array.
'''

def merge_two(A, B, n):
  i = j = 0
  words_so_far = {}
  merged = []


  while len(merged) < n and i < n and j < n:
    if A[i] in words_so_far:
      i += 1
    if B[j] in words_so_far:
      j += 1
    if A[i] < B[j]:
       merged.append(A[i])
       words_so_far[A[i]] = True
       i += 1
    else:
       merged.append(B[j])
       words_so_far[B[j]] = True
       j += 1


  return merged 


'''
'Hello', 2 --> 'lloHe'
'Hello' 3 --> 'loHel'
'Hello', 1117 --> 'lloHe'
'Hi', 1 --> 'iH'
'i', 17 --> 'i'
'''
def rotate_left(str, n):
	if len(str) < 2:
		return str

	return str[n%len(str):] + str[:n%len(str)]


'''
dependencies will be a dict in the form:
{0:[1, 2], 1:[3], 2:[3], 3:[4], 4:[]}

For i:[j_1, ..., j_n], each of the j indices depend on i
'''
def package_dependencies(dependencies):
	package_order = []
	explored = [False]*len(dependencies)

	for node in range(len(dependencies)):
		if not explored[node]:
			package_dependencies_DFS(node, dependencies, explored, package_order)

	package_order.reverse() # nodes will be inserted in the reverse order
							# of the "finishing times"
	return package_order

def package_dependencies_DFS(s, dependencies, explored, package_order):
	explored[s] = True

	for node in dependencies[s]:
		if not explored[node]:
			package_dependencies_DFS(node, dependencies, explored, package_order)

	package_order.append(s)	


if __name__ == '__main__':
	'''
	print(count_permutations_in_string('aba', 'abadaba'))
	print(count_permutations_in_string('aba', 'aabdaba'))
	print(count_permutations_in_string('hi', 'hello'))
	print(count_permutations_in_string('hi', 'hihihello')) # interesting edge case! Refactored to catch 'hi', 'ih', 'hi', 'ih'
	
	print(merge_two(["a", "c", "z"], ["c", "f", "z"], 3)) # ["a", "c", "f"]
	print(merge_two(["x", "y", "z"], ["a", "b", "z"], 3)) #  ["a", "b", "x"]
	print(rotate_left('Hello', 2)) # 'lloHe'
	print(rotate_left('Hello', 3)) # 'loHel'
	print(rotate_left('Hello', 1117)) # 'lloHe'
	print(rotate_left('Hi', 1)) # 'iH'
	print(rotate_left('i', 17)) # 'i'
	print(rotate_left('', 2)) # ''
	
	'''
	print(package_dependencies({0:[1, 2], 1:[3], 2:[3], 3:[4], 4:[]})) # [0, 2, 1, 3, 4] and [0, 1, 2, 3, 4] are valid build orders

