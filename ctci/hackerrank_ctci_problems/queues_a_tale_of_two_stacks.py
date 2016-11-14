class MyQueue(object):
    def __init__(self):
        self.incoming = []
        self.outgoing = []
    
    def peek(self):
        if self.outgoing:
            return self.outgoing[len(self.outgoing) - 1]
        return self.incoming[0]
        
    def pop(self):
        if self.outgoing:
            self.outgoing.pop()
        else:
            while self.incoming:
                self.outgoing.append(self.incoming.pop())
            self.outgoing.pop()
        
    def put(self, value):
        self.incoming.append(value)

'''
# (!) Another way:
class MyQueue(object):
    def __init__(self):
        self.data = []
    
    def peek(self):
        return self.data[0]
        
    def pop(self):
        self.data = self.data[1:]
        
    def put(self, value):
        self.data.append(value)
'''

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
