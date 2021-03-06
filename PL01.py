class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        find_list = []
        node = self.head
        while node is not None:
            if node.value == val:
                find_list.append(node)
            node = node.next

        return find_list

    def delete(self, val, all=False):
        if all == False:
            node = self.find(val)
            if node is not None:

                node_prev = self.head
                if  node_prev is not None and node_prev == node:
                    self.head = node.next
                    if self.tail == node:
                        self.tail = None
                    return True
                while node_prev is not None:

                    if node_prev.next == node:
                        node_prev.next = node.next
                        if node == self.tail:
                            self.tail = node_prev

                    node_prev = node_prev.next

        else:
            find_list = self.find_all(val)
            for nod in find_list:
                node = self.head
                if node == nod:
                    self.head = nod.next
                if nod is not self.tail:
                    while node is not None and node is not self.tail:
                        # if self.tail not nod #node.next is not None:

                        if node.next == nod:
                            node.next = nod.next
                            #break
                            iiii=777
                        node = node.next

                else:

                    while node is not None:
                        # if self.tail not nod #node.next is not None:
                        if self.len() > 1:

                            if node.next == nod:
                                node.next = None
                                self.tail = node
                                break
                            node = node.next
                        else:
                            self.__init__()
                            break
                        #   self.tail = node
                # node = self.find(val)
                # node_prev = self.head

    def clean(self):
        self.__init__()

    def len(self):

        node = self.head
        i = 0
        while node is not None:
            i = i + 1
            node = node.next

        return i

    def insert(self, afterNode, newNode):

        if afterNode == None:
            self.add_in_tail(newNode)

        else:

            newNode.next = afterNode.next
            afterNode.next = newNode
            if afterNode == self.tail:
                #self.tail = newNode
                self.add_in_tail(newNode)
