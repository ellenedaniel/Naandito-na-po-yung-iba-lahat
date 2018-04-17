#Binary Tree
#Ellene Gay S. Daniel


class Node:
    def __init__(self, val):
        self.a = None
        self.w = None
        self.e = val

class Binary_Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.e):
            if(node.a != None):
                self._add(val, node.a)
            else:
                node.a = Node(val)
        else:
            if(node.w != None):
                self._add(val, node.w)
            else:
                node.w = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.e):
            return node
        elif(val < node.e and node.a != None):
            self._find(val, node.l)
        elif(val > node.e and node.w != None):
            self._find(val, node.w)

    def deleteBinary_Tree(self):
        # garbage collector will do this for us.
        self.root = None

    def printBinary_Tree(self):
        if(self.root != None):
            self._printBinary_Tree(self.root)

    def _printBinary_Tree(self, node):
        if(node != None):
            self._printBinary_Tree(node.a)
            print (str(node.e) + ' ')
            self._printBinary_Tree(node.w)


tree = Binary_Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)


tree.printBinary_Tree()

print(tree.find(3).e)

print(tree.find(10))

tree.deleteBinary_Tree()

tree.printBinary_Tree()
