class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data==data_after:
            self.insert_at_begining(data_to_insert)
            return

        itr = self.head
        while itr:
            if(itr.data==data_after):
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next      

    def remove_by_value(self, data):
        if self.head is None:
            return 
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if(itr.next.data==data):
                itr.next=itr.next.next
                break
            itr = itr.next

   # Reversing a Linked List
    def reverseList(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        prev = None
        current = self.head
        
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return

    # Finding the middle element of the linked list
    # we have two pointer, we move first by one and second by two so when second completes first will be at middle
    def middleNode(self):
        fast_pointer = slow_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer.data
         
if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_values([1,2,3,4])
    ll.print()
    ll.reverseList()
    ll.print()
    print(ll.middleNode())
    # ll.print()
    # ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.print()
    # ll.remove_by_value("banana") # remove orange from linked list
    # ll.print()