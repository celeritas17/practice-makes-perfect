'''
[5] Write a function to perform integer division without using either the / or * operators. Find a fast way to do it.

[5] There are 25 horses. At most, 5 horses can race together at a time. You must determine the fastest, second fastest, 
and third fastest horses. Find the minimum number of races in which this can be done.



Have horses h1,...,h25

[h1, h2, h3]  [h6, h7, h8]  [h11, h12, h13]  [h16, h17, h18]  [h21, h22, h23]

[h1, h2, h3] [h8, h11, h12] [h17, h18, h21]

[h1, h2, h3]  [h12, h17, h18]

[]

[]


'''

def division(dividend, divisor):
	if divisor == 0:
		return None
	if abs(divisor) > abs(dividend):
		return 0

	parity = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1

	dividend = abs(dividend)
	divisor = abs(divisor)

	return (1 + division(dividend - divisor, divisor)) if parity == 1 else -(1 + division(dividend - divisor, divisor))

if __name__ == '__main__':
	print(division(-4, -16))
