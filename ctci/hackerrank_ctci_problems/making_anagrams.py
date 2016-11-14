def char_map(str):
    chars = {}
    for c in str:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
    
def number_needed(a, b):
    remove_number = 0
    commons = {} # occur in a and b; difference in counts already processed
    a_char_map = char_map(a)
    b_char_map = char_map(b)
    
    for c in a_char_map:
        if c not in commons:
            if c in b_char_map:
                remove_number += abs(a_char_map[c] - b_char_map[c])
                commons[c] = True
            else:
                remove_number += a_char_map[c]
                
    for c in b_char_map:
        if c not in commons:
            if c in a_char_map:
                remove_number += abs(a_char_map[c] - b_char_map[c])
                commons[c] = True
            else:
                remove_number += b_char_map[c]
    
    return remove_number
    
a = 'blah'#input().strip()
b = 'ha'#input().strip()

print(number_needed(a, b))