#Soal Bagian1
class Pixel():
    def __init__(self,name_pixel,x,y):
        self.name = name_pixel
        self.locate_x = x
        self.locate_y = y
    def moveLeft(self,n):
        self.locate_x -= n
    def moveRight(self,n):
        self.locate_x += n
    def moveForward(self,n):
        self.locate_y += n
    def moveBackward(self,n):
        self.locate_y -= n
    def distance(self,pixel2):
        x1 = self.locate_x
        x2 = pixel2.locate_x
        y1 = self.locate_y
        y2 = pixel2.locate_y
        temp = (((x1-x2)**2)+((y1-y2)**2))**0.5
        return temp
    def display(self):
        print(self.name,": ({},{})".format(self.locate_x,self.locate_y))

pix1 = Pixel("point 1",5,7)
pix2 = Pixel("point 2",6,5)

print("\nBagian1\n")
pix1.display()
pix2.display()
pix1.moveBackward(5)
pix1.display()
jarak = pix1.distance(pix2)
print("jarak =",jarak)
pix2.moveForward(3)
pix2.display()
pix2.moveLeft(1)
pix2.display()
pix2.moveRight(15)
pix2.display()

#Soal Bagian2
def remainderFunction(data,num): #Membuat hash dari data mod num
    return(data%num)

def strVal(strData): #Hash for string
    temp = 0
    for x in range(len(strData)):
        temp += ord(strData[x])
    return(temp)

def createHashTable(num): #Membuat table untuk store data hash, range(num)
    temp = []
    for i in range(num):
        temp.append([None])
    return(temp)

def putData(data,table): #Function untuk store data ke dlm table
    for i in range(len(data)):
        int_data = strVal(data[i])
        ind = remainderFunction(int_data,len(table)) #Deklarasi var sbgai membuat nilai hash
        temp = []
        temp.append(data[i])
        if type(table[ind]) == list and len(table[ind]) >= 1 and (table[ind] != [None]) : #Chaining
            table[ind].append(data[i])
        else:
            table[ind] = temp
          
    return(table)

def searchHash(data,table): #Matching data dari dlm table, output berupa boolean
    int_data = strVal(data)
    hashVal = remainderFunction(int_data, len(table))
    if data in table[hashVal]:
        find_index = table[hashVal].index(data)
        return("Data '{}' terdapat di slot {} indeks: {}".format(data,hashVal,find_index))
    else:
        return("Data '{}' tidak ada".format(data))

print("\nBagian2\n")
data = ["diah","dina","andi","hadi","tiara"]
hashTable = createHashTable(11)
hashTable = putData(data,hashTable)
print(searchHash("indah",hashTable))
print(searchHash("dina",hashTable))
print(searchHash("andi",hashTable))
print(searchHash("hadi",hashTable))
print(searchHash("diah",hashTable))

#Soal Bagian3
class BinaryTree:
    #constructor
    def __init__(self,data):
        self.key = data
        self.RightChild = None
        self.LeftChild = None
    def insertLeft(self,new_tree):
        self.LeftChild = new_tree
    def insertRight(self,new_tree):
        self.RightChild = new_tree

def parsingBinTree(binTree):
    left = binTree.LeftChild
    right = binTree.RightChild
    if (left != None) or (right != None):
        Node = binTree.key
        if left != None:
            print("Left Child of Node - {} is : {}".format(Node,left.key))
            parsingBinTree(left)
        if right != None:
            print("Right Child of Node - {} is : {}".format(Node,right.key))
            parsingBinTree(right)
    else:
        Node = binTree.key
        print("Node - {} is a leaf".format(Node))

#Tree1
tree1 = BinaryTree("a")
child1 = BinaryTree("b")
child2 = BinaryTree("c")
leaf1 = BinaryTree("d")
leaf2 = BinaryTree("e")
leaf3 = BinaryTree("f")
leaf4 = BinaryTree("g")
#Child1
tree1.insertLeft(child1)
tree1.insertRight(child2)
#Leaf1
child1.insertLeft(leaf1)
child1.insertRight(leaf2)
child2.insertLeft(leaf3)
child2.insertRight(leaf4)
print("\nBagian3\n\nNo_1")
parsingBinTree(tree1)

#Tree2
tree2 = BinaryTree("a")
child1 = BinaryTree("b")
child2 = BinaryTree("c")
child3 = BinaryTree("d")
leaf1 = BinaryTree("f")
leaf2 = BinaryTree("g")
#Child2
tree2.insertLeft(child1)
tree2.insertRight(child2)
#Child2_1
child2.insertLeft(child3)
#Leaf2
child3.insertLeft(leaf1)
child3.insertRight(leaf2)
print("\nNo_2")
parsingBinTree(tree2)

#Tree3
tree3 = BinaryTree("a")
child1 = BinaryTree("b")
leaf1 = BinaryTree("c")
#Child3
tree3.insertLeft(child1)
#Leaf3
child1.insertRight(leaf1)
print("\nNo_3")
parsingBinTree(tree3)