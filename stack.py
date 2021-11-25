class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def __str__(self):
      cur = self.head.next
      out = ""
      while cur:
         out += str(cur.data) + "->"
         cur = cur.next
      return out[:-3]  


    def isEmpty(self):
        return self.size==0
    
    def getsize(self):
        return self.size
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Underflow")
        return self.head.next.data

    def push(self,value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size +=1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Underflow")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size-=1
        return remove.data


if __name__=="__main__":
    stack = Stack()
    for i in  range(1,11):
        stack.push(i)
    
    print(f"Stack: {stack}")
    
    print(stack.pop())