class Node(object):
    def __init__(self, char, children={}, is_word=False):
        self.char = char
        self.children = children
        self.is_word = is_word
    
    def __repr__(self):
        return '{' + self.char + ', ' + str(self.children) + ', ' + str(self.is_word) + '}' 

class Trie(object):
    def __init__(self):
        self.root = Node(str(-1), {}, False)
    
    def add(self, word):
        node = self.root
        index = 0
        if node.children:
            while word[index] in node.children:
                node = node.children[word[index]]
                index += 1
            while index < len(word) - 1:
                node.children[word[index]] = Node(word[index], {}, False)
                node = node.children[word[index]]
                index += 1
            node.children[word[index]] = Node(word[index], {}, True)
        else:
            for char in word[:len(word) - 1]:
                node.children[char] = Node(char, {}, False)
                node = node.children[char]
            node.children[word[len(word) - 1]] = Node(word[len(word) - 1], {}, True)
    
    def count_descendant_words(self, node):
        count = 1 if node.is_word else 0
        if not node.children:
            return count
             
        for child in node.children:
            count += self.count_descendant_words(node.children[child])
        
        return count
    
    def find(self, word):
        node = self.root
        index = 0
        while index < len(word):
            if word[index] in node.children:
                node = node.children[word[index]]
                index += 1
            else:
                break
        
        if index < len(word):
            return 0
        else:
            return self.count_descendant_words(node)
        

trie = Trie()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'find':
        print(trie.find(contact))
    if op == 'add':
        trie.add(contact)
        