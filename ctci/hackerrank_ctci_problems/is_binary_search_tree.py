""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

MAX = 10000000
MIN = -10000000

'''
Don't mess around trying random things when you're stuck--
think about (draw!) an example and use it to walk through
your logic.
'''

def traverse(node, tree_max, tree_min):
    if node == None: 
        return True
    if node.data > tree_max:
        return False
    if node.data < tree_min:
        return False
    
    return traverse(node.right, tree_max, node.data + 1) and traverse(node.left, node.data - 1, tree_min)

def check_binary_search_tree_(root):
    if root == None: return True
    return traverse(root.right, MAX, root.data + 1) and traverse(root.left, root.data - 1, MIN)