from queue import PriorityQueue


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


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(
            self.head)  # set new_node tro den phan tu dau tien (self.head tro den phan tu dau tien cua list)
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
        else:  # cho du current la phan tu cuoi cung thi current.getNext() se return None
            previous.setNext(current.getNext())

    def insert_tail(self, item):
        current = self.head
        previous = None
        while current:
            previous = current
            current = current.getNext()
        # after the while, the previous will be the last element
        new_node = Node(item)  # new_node will have default Next =None
        previous.setNext(new_node)

    def listall(self):
        current = self.head
        while current:
            print(current.getData())
            current = current.getNext()


class Solution(object):
    def MergeKLists(self, linkedlist1, linkedlist2, linkedlist3):
        self.q = []
        iter1 = linkedlist1.head
        while iter1:
            self.q.append(iter1.getData())
            iter1 = iter1.getNext()
        iter2 = linkedlist2.head
        while iter2:
            self.q.append(iter2.getData())
            iter2 = iter2.getNext()
        iter3 = linkedlist3.head
        while iter3:
            self.q.append(iter3.getData())
            iter3 = iter3.getNext()
        # for i in kwargs:
        #     iter = i.head
        #     while iter:
        #         self.nodes.append(iter.getData())
        #         iter = iter.getNext()
        print(self.q)
        self.q = sorted(self.q)
        head = point = LinkedList()
        for i in self.q:
            point.insert(i)
        point.listall()

    # using PriorityQueue.
    # from queue import PriorityQueue
    def MergeKLists2(self, linkedlist1, linkedlist2, linkedlist3):
        q = PriorityQueue()
        iter1 = linkedlist1.head
        while iter1:
            q.put((iter1.getData(), iter1))
            iter1 = iter1.getNext()
        iter3 = linkedlist3.head
        while iter3:
            q.put((iter3.getData(), iter3))
            iter3 = iter3.getNext()
        iter2 = linkedlist2.head
        while iter2:
            q.put((iter2.getData(), iter2))
            iter2 = iter2.getNext()
        print(q)
        head = point = LinkedList()
        while not q.empty():
            data, Node = q.get()# why
            print(data)
            point.insert(LinkedList(data))
        point.listall()


linkedlist1 = LinkedList()
linkedlist1.insert(1)
linkedlist1.insert(3)
linkedlist1.insert(6)
linkedlist1.insert(12)
linkedlist1.insert(25)
linkedlist1.insert(67)
print("list1", linkedlist1.listall())
linkedlist2 = LinkedList()
linkedlist2.insert(3)
linkedlist2.insert(5)
linkedlist2.insert(15)
linkedlist2.insert(18)
linkedlist2.insert(25)
linkedlist2.insert(69)
print("list2", linkedlist2.listall())
linkedlist3 = LinkedList()
linkedlist3.insert(9)
linkedlist3.insert(17)
linkedlist3.insert(25)
linkedlist3.insert(28)
linkedlist3.insert(29)
linkedlist3.insert(49)
print("list3", linkedlist3.listall())

solution = Solution()
solution.MergeKLists2(linkedlist1, linkedlist2, linkedlist3)
