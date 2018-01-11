class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)  # set new_node tro den phan tu dau tien (self.head tro den phan tu dau tien cua list)
        self.head = new_node  # head of the list tro den new_node

    def size(self):
        current = self.head  # bat dau tu phan tu dau tien
        count = 0
        while current:  # break when current=None, tuc la phan tu cuoi cung
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if (current.getData() != item):
                current = current.getNext()
            else:
                found = True
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if (current.getData() != item):
                previous = current
                current = current.getNext()
            else:
                found = True
        if current == None:  # if item is not in the list
            raise ValueError("Data is not in the list")
        # if item is the first element
        if previous == None:
            self.head = current.getNext()
        else: #cho du current la phan tu cuoi cung thi current.getNext() se return None
            previous.setNext(current.getNext())

    def insert_tail(self,item):
        current = self.head
        previous=None
        while current:
            previous=current
            current=current.getNext()
        # after the while, the previous will be the last element
        new_node=Node(item) #new_node will have default Next =None
        previous.setNext(new_node)
    def listall(self):
        current = self.head
        while current:
            print(current.getData())
            current = current.getNext()

linkedlist = LinkedList()
linkedlist.insert(31)
linkedlist.insert(77)
linkedlist.insert(17)
linkedlist.insert(93)
linkedlist.insert(26)
linkedlist.insert(54)

print(linkedlist.size())
# print(linkedlist)
print(linkedlist.search(93))
print(linkedlist.search(100))

linkedlist.insert(100)
print(linkedlist.search(100))
print(linkedlist.size())

linkedlist.remove(54)
print(linkedlist.size())
linkedlist.remove(93)
print(linkedlist.size())
print(linkedlist.search(93))
linkedlist.remove(26)
print(linkedlist.size())
linkedlist.listall()
linkedlist.insert_tail(111)
linkedlist.listall()