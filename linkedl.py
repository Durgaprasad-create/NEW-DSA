# linkedlist
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        llstr += 'None'
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self,index,data):
        if index<0 or index > self.length():
            raise Exception("invalid index")
        if index==0:
            self.insert_at_begining(data)
            return
        count=0
        itr=self.head
        while itr:
            if count== index -1:
                node=Node(data,itr.next)
                itr.next=node
                break

            itr=itr.next
            count=+1
        

if __name__ == '__main__':
    ll = linked_list()
    ll.insert_values(["mango", "apple", "orange", "banana"])
    # ll.remove_at(2)  # Removes "orange"
    ll.insert_at(2,"kiwi")
    ll.print()
