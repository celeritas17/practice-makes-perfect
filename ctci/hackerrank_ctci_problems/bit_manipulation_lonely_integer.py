#!/bin/python3

'''
(!) (!) (!) Use divide and conquer paradigm (!) (!) (!)
-> Remember: A is a list of odd length (and always non-empty)
'''

def lonely_integer(A):
	if len(A) == 1:
		return A[0]

	return lonely_integer(A[0:len(A)//2]) ^ lonely_integer(A[len(A)//2:])

# chars is a list of ascii chars
def lonely_char(chars):
	if len(chars) == 1:
		return ord(chars[0])

	return lonely_char(chars[0:len(chars)//2]) ^ lonely_char(chars[len(chars)//2:])
    
'''
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
'''
a = [1, 1,2, 3,3, 4, 4]
b = ['a', 'a', 'b', 'b', 'c', 'd', 'd', 'e', 'e']
print(lonely_integer(a))
print(chr(lonely_char(b)))
