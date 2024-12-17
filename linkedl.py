# linkedlist
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+ "-->"
            itr=itr.next
        llstr +='None'
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
           self.head=Node(data,None)
           return
       
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)


    def length(self):
        count=0
        itr=self.head
        while itr:
            count += 1
            itr=itr.next
        return count
    
    def insert_at(self,data,index):
        if index < 0 or index > self.length():
            raise Exception ("invalid index!")
        if index == 0:
            self.insert_at_begining(data)
            return
        count =0
        itr= self.head
        while itr:
            if count == index -1:
                node= Node(data,itr.next)
                break
            itr = itr.next
            count +=1

    def remove_at(self,index):
        if index < 0 or index > self.length():
            raise Exception ("invalid index!")
        if index ==0:
            self.head=self.head.next
            return

        count=0
        itr =self.head
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self,data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr=self.head
        while itr.next:
            if itr.next.data == data:
                itr.next=itr.next.next
                break
            itr=itr.next


ll=Linkedlist()
ll.insert_values(["java","python","CSS"])
ll.insert_after_value("python","html")
ll.remove_by_value("java")
ll.print()