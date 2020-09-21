class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next_ = next_

class Linked_List:
    def __init__(self):
        self.head=None

    def add_to_beginning(self, value):
        node = Node(value, self.head)
        self.head = node
    
    def add_to_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        itr = self.head
        while itr.next_:
            itr = itr.next_
        
        itr.next_ = Node(value, None)

    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next_     
        return length

    def remove_at(self, index):
        if index > self.get_length() or index < 0:
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next_
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next_ = itr.next_.next_ 
                break 
            itr = itr.next_
            count += 1

    def remove_value(self, value):
        if self.head.value == value:
            self.head = self.head.next_
            return
        itr = self.head
        while itr.next_:
            if itr.next_.value == value:
                itr.next_ = itr.next_.next_
                return
            itr = itr.next_

    
    def insert_at(self, index, value):
        if index > self.get_length() or index < 0:
            raise Exception("Invalid index")
        if index == 0:
            self.add_to_beginning(value)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(value, itr.next_)
                itr.next_=node
                break
            itr = itr.next_
            count += 1

    def print_list(self):
        if self.head is None:
            print("The list is empty.")
            return
        itr = self.head
        while itr:
            print(itr.value)
            itr = itr.next_


list1 = Linked_List()
list1.add_to_beginning(12)
list1.add_to_end(13)
list1.add_to_end(14)
list1.add_to_end(15)
list1.add_to_end(16)
list1.print_list()
list1.remove_value(12)
print("after action:")
list1.print_list()