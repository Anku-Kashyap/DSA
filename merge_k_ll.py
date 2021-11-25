class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:

    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next=  self.head
        self.head = new_node

    def insert_after(self,prev,data):
        if prev is  None:
            print("Not found")
            return
        
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 

        last = self.head
        while last.next:
            last=  last.next
        
        last.next = new_node

    def delete_node(self,key):
        temp  = self.head

        if temp is not None:
            if temp.data == key:
                self.head= temp.next
                temp = None
                return
            
        
        while  temp is not None:
            if temp.data ==key:
                break
            prev = temp
            temp = temp.next
        
        if temp==None:
            return 

        prev.next = temp.next

        temp = None

   
        
    def del_pat_node(self,position):
        if self.head == None:
            return
        
        temp = self.head

        if position==0:
            self.head = temp.next
            temp = None
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                return
        
        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None
        temp.next = next

    def del_ll(self):
        curr = self.head
        while curr:
            prev = curr.next

            del curr.data
            curr = prev


    def count_ll(self,node):
        if not node:
            return 0
        else:
            return 1+self.count_ll(node.next)

    def getnth_node(self,head,position):
        if head:
            c = 0
            if c==position:
                return head.data
            else:
                
                self.getnth_node(head.next,position-1)


    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        
if __name__=='__main__':

    llist= linked_list()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next= second
    second.next = third
    llist.push(5)
    llist.insert_after(llist.head,10)
    llist.append(12)
    

    llist.printlist()
    print("\n")
    a = llist.getnth_node(llist.head,3)
    print(a)
   

    llist.printlist()