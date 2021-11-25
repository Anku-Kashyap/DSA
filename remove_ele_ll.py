class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 

        last = self.head
        while last.next:
            last=  last.next
        
        last.next = new_node
    
    def remove_sum_zero(self,head):

        def yielder(n):
            while n:
                yield n
                n = n.next

        A,S=[],[]
        d = {0:-1}
        t = 0
        for n in yielder(head):
            t+=n.data
            if t in d:
                for _ in range(d[t]+1,len(A)):
                    A.pop()
                    d.pop(S.pop())

                t = S[-1] if S else 0
            else:
                A.append(n)
                S.append(t)
                d[t]= len(A)-1

        A.append(None)
        for i,x in enumerate(A[:-1]):
            x.next = A[i+1]
        return A[0]


def printlist(c):
        while c.next:
            print(c.data,end=" ")
            c = c.next
        print(c.data)
    
if __name__=='__main__':
    llist = linked_list()
    llist.head = Node(9)
    for i in range(int(input("Enter the no you want to add: "))):
        a = int(input())
        llist.append(a)
    k = 0
    c = llist.remove_sum_zero(llist.head)
    if c!=None:
        printlist(c)