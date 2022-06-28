class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head==None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def insertPrevious(self, item, index):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == index:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            item.setNext(self.head)
            self.head = item
        else:
            previous.setNext(item)
            item.setNext(current)
    def insertNext(self, item, index):
        current = self.head
        after = current.getNext()
        found = False
        while not found:
            if current.getData() == index:
                found = True
            else:
                current = after
                after = current.getNext()
        if after == None:
            current.setNext(item)
        else:
            current.setNext(item)
            item.setNext(after)



myls = LinkedList()
myls.add(1)
myls.add(2)
myls.add(3)
myls.add(4)
myls.add(5)
myls.display()

print('')
print('=========================')
print('Insert Previous')
a=int(input('Data yang ingin dimasukkan = ' ))
b=int(input('Sebelum Data = ' ))
myls.insertPrevious(Node(a),b)
myls.display()
print('')
print('=========================')
print('Insert Next')
c=int(input('Data yang ingin dimasukkan = ' ))
d=int(input('Setelah Data = ' ))
myls.insertNext(Node(c),d)
myls.display()