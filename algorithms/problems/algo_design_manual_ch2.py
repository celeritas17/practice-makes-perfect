'''
function mystery(n) r := 0
for i := 1 to n − 1 do 
  for j := i + 1 to n do 
     for k := 1 to j do
       r := r + 1 

 return(r)

'''

def mystery(n):
	r = 0
	for i in range(0, n):
		for j in range(i, n):
			for k in range(0, j):
				r += 1

	return r

def pesky(n):
	r = 0
	for i in range(n):
		for j in range(i):
			for k in range(j, i + j + 1):
				r += 1
	return r


'''
You have a 100-story building and a couple of marbles. You must identify the lowest floor 
for which a marble will break if you drop it from this floor. How fast can you find this 
floor if you are given an infinite supply of marbles? What if you have only two marbles?
'''

'''
2-43. [5] You are given a set S of n numbers. You must pick a subset S′ of k numbers from S 
such that the probability of each element of S occurring in S′ is equal (i.e., each is 
selected with probability k/n). You may make only one pass over the numbers. What if n is unknown?
'''

'''
2-47. [5] You are given 10 bags of gold coins. Nine bags contain coins that each weigh 10 grams. 
One bag contains all false coins that weigh one gram less. You must identify this bag in just one 
weighing. You have a digital balance that reports the weight of what is placed on it.
'''