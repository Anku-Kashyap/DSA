from types import new_class


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class  linked_list:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return 
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node


        

    def sortedmerge(self,a,b):
        if a==None:
            return b
        
        if b==None:
            return a

        if a.data<=b.data:
            result = a
            result.next = self.sortedmerge(a.next,b)
        else:
            result = b
            result.next = self.sortedmerge(a,b.next)
        return result

    def mergesort(self,h):
        
        if h==None or h.next==None:
            return h
        
        middle = self.getmiddle(h)
        nexttomiddle = middle.next

        middle.next = None
        left = self.mergesort(h)
        right = self.mergesort(nexttomiddle)

        sortedlist = self.sortedmerge(left,right)

        return sortedlist
    
    def getmiddle(self,head):
        if head ==None:
            return head
        
        slow = head
        fast = head
        while fast.next!= None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        

    def printlist(self,head):
        if head is None:
            print(' ')
            return
        curr= head
        while curr:
            print(curr.data,end=" ")
            curr = curr.next

        print(' ')

if __name__ == '__main__':
    llist = linked_list()
    for i in range(int(input("enter the no of element :"))):
        a=  int(input())
        llist.append(a)
    
    llist.head = llist.mergesort(llist.head)
    llist.printlist(llist.head)
    



