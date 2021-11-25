class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, a):
        new_node = Node(a[0])
        if self.head is None:
            self.head = new_node

        last  = self.head
        for i in range(1, len(a)):
            new_node = Node(a[i])

            last.next = new_node
            last = new_node
        
    

    def reverse(self,head,k):
        if head==None:
            return None
        prev = None
        next = None
        current = head
        count = 0
        
        while current is not None and count<k:
            next= current.next
            current.next = prev
            prev = current
            current = next
            count +=1

        if next is not None:
            head.next = self.reverse(next,k)
        
        return prev
    
    def printlist(self):
        top = self.head
        while top:
            print(top.data,end=" ")
            top = top.next



if __name__ == '__main__':
    a = [1,2,2,4,5,6,7,8]
    llist = Linkedlist()
    llist.append(a)
    
    llist.head = llist.reverse(llist.head,4)
   
    llist.printlist()
    