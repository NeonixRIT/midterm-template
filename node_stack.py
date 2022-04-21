"""
Provides a node-based implementation of a stack data structure.

@author GCCIS Faculty
"""
import node

class Stack:
    slots = ["__top", "__size"]

    def __init__(self):
        self.__top = None
        self.__size = 0


    def __eq__(self, other) -> bool:
        if type(other) != type(self):
            return False
        curr_self = self.__top
        curr_other = other.__top
        while curr_self and curr_other:
            if curr_self != curr_other:
                return False
            curr_self = curr_self.get_next()
            curr_other = curr_other.get_next()
        return True


    def size(self):
        return self.__size


    def push(self, value):
        new_node = node.Node(value, self.__top)
        self.__top = new_node
        self.__size += 1


    def pop(self):
        if self.__top is None:
            raise IndexError("pop from empty stack")
        top = self.__top
        value = top.get_value()
        self.__top = top.get_next()
        self.__size -= 1
        return value


    def peek(self):
        if self.__top is None:
            raise IndexError("peek from empty stack")
        value = self.__top.get_value()
        return value


    def is_empty(self):
        return self.__top is None


    def __repr__(self):
        string = "["
        node = self.__top
        if node is not None:
            string += str(node.get_value())
            node = node.get_next()
            while node is not None:
                string += ", " + str(node.get_value())
                node = node.get_next()
        string += "]"
        return string


def fromList(a_list: list) -> Stack:
    result = Stack()
    [result.push(ele) for ele in a_list[::-1]]
    return result
