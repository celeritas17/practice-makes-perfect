def get_word_counts(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

def ransom_note(magazine, ransom):
    ransom_word_counts = {}
    magazine_word_counts = get_word_counts(magazine)
    
    for word in ransom:
        if word not in magazine_word_counts:
            return False
        if word in ransom_word_counts:
            ransom_word_counts[word] += 1
            if ransom_word_counts[word] > magazine_word_counts[word]:
                return False
        else:
            ransom_word_counts[word] = 1
     
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print('Yes')
else:
    print('No')