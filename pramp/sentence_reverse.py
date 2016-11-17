'''
  You are given an array of characters arr, which consists of sequences of 
characters separated by space characters. Each space-delimited sequence of 
characters defines a word.
  How can you most efficiently reverse the order of the words in the array?
Explain and implement your solution. Lastly, analyze its time and space 
complexities.

For example:
[ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

would turn into:
[ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'e', 'r', 'f', 'e', 'c', 't' ]
'''

# what if arr has all ‘ ‘ (spaces)? What if arr is length 0? Or has just 1 word?

# assume arr is not all spaces, does not have a leading space, 
# does not have a trailing space, and does not have consecutive spaces.
def sentence_reverse(arr):
  if len(arr) < 3:
    return arr
  arr.reverse()
  
  word_boundary = 0
  word_front = 0
  word_back = 0


  while word_boundary < len(arr):
    while word_back < len(arr) and arr[word_back] != ' ':
      word_back += 1
  
    # save word_boundary at the start of next word
    # if it exists
    word_boundary = word_back + 1
  
    # set word_back to the end of the current word
    word_back -= 1

    while word_front < word_back:
      temp = arr[word_front]
      arr[word_front] = arr[word_back]
      arr[word_back] = temp
      word_front +=1
      word_back -= 1

    word_front = word_back = word_boundary


if __name__ == '__main__':
	arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
	print(arr)
	sentence_reverse(arr)
	print(arr)
