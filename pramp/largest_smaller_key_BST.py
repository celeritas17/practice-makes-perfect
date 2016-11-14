'''
Given a root of a binary search tree and a key x, 
find the largest key in the tree that is smaller than x.
'''

def largest_smaller_key(node, x):
	result = None

	while node != None:
		if node.data < x:
			result = node.data
			node = node.right
		else:
			node = node.left

	return result