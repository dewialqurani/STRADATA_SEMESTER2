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