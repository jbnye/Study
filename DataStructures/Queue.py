
class Q:
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.append(item)
        return self
    
    def pop(self):
        if(len(self.queue) != 0):
            self.queue.reverse()
            self.queue.pop()
            self.queue.reverse()
            return self
        return None
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if(len(self.queue) != 0):
            return self.queue[0]
        return None
        
queue = Q()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
print(queue.peek())
print(queue.size())
queue.pop()
print(queue.size())
print(queue.peek())
