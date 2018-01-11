# binary search tree
class Node:
    def __init__(self, val):
        self.v = val
        self.r = None
        self.l = None


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:  # node not null
            self._add(val, self.root)

    def _add(self, val, node):  # this will be called recursively until we find suitable position
        if val < node.v:
            if node.l != None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        if val >= node.v:
            if node.r != None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if (self.root == None):
            return None
        else:
            return self._find(val, self.root)

    def _find(self, val, node):
        if node == None:
            return None
        elif node.v == val:
            return node
        elif val < node.v:
            self._find(val, node.l)
        elif val > node.v:
            self._find(val, node.r)

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node != None:
            self._printTree(node.l)
            yield str(node.v) + ''
            self._printTree(node.r)

    def deleteTree(self):
        self.root = None

    def longestUnivaluePath(self):
        self.ans = 0

        def arrow_length(node):
            if node == None: return 0
            left_length = arrow_length(node.l)
            right_length = arrow_length(node.r)
            left_arrow = right_arrow = 0
            if node.l != None and node.l.v == node.v:
                left_arrow = left_length + 1
            if node.r != None and node.r.v == node.v:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            print("ans {},left {}, right {}, type left {}, type right{}".format(self.ans, left_arrow, right_arrow, type(left_arrow),type(right_arrow)))
            return max(left_arrow, right_arrow)# we need to return it to asign to left_length and right_length

        arrow_length(self.root)
        return self.ans


tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.add(2)
tree.add(2)
tree.add(2)
tree.printTree()
print(tree.longestUnivaluePath())
