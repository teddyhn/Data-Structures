import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.dft_stack = Stack()
        self.bft_queue = Queue()

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        self.dft_stack.push(node)
        if node.left is not None:
            self.in_order_print(node.left)
        elif node.right is not None:
            temp = self.dft_stack.pop()
            print(temp.value)
            self.in_order_print(node.right)
        else:
            print(node.value)
            self.dft_stack.pop()
            prev = self.dft_stack.pop()
            print(prev.value)
            if prev.right is not None:
                self.in_order_print(prev.right)
            else:
                final = self.dft_stack.pop()
                print(final.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        temp = node
        while temp is not None:
            print(temp.value)
            if temp.left is not None:
                self.bft_queue.enqueue(temp.left)
            if temp.right is not None:
                self.bft_queue.enqueue(temp.right)
            temp = self.bft_queue.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        temp = node
        while temp is not None:
            print(temp.value)
            if temp.left is not None and temp.right is not None:
                self.dft_stack.push(temp)
                temp = temp.right
            elif temp.right is not None:
                temp = temp.right
            elif temp.left is not None:
                temp = temp.left
            else:
                prev = self.dft_stack.pop()
                if prev is not None:
                    temp = prev.left
                else:
                    break


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
