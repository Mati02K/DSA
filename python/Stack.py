from collections import deque
# This Deque opration uses Boubly Linked List for stroing the data in the stack thus overcoming the problem faced by the Linked List
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def reverse_string(self,data):
        output_string=""
        for i in range(0,len(data)-1):
            self.push(data[i])
        for j in range(0,len(data)-1):
            output_string += self.pop()
        return output_string



if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(9)
    s.push(34)
    s.push(78)
    s.push(12)
    print(s.peek())
    print(s.pop())
    print(s.is_empty())
    print(s.reverse_string("We will conquere COVID-19"))
   

