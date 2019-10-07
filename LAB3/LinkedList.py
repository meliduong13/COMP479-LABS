from Node import *


class LinkedList:
    # "constructor to initiate this object"
    def __init__(self):
        self.head = None
        self.tail = None
        return

    # "add an item at the end of the list"
    def add(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    # "outputs the list (the value of the node, actually)"
    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.filename)
            current_node = current_node.next
        return

    # "returns the number of list items"
    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            # increase counter by one
            count = count + 1
            # jump to the linked node
            current_node = current_node.next
        return count

    def union_with_another_list(self, another_list):
        mylist = LinkedList()
        current_node_self = self.head
        current_node_another_list = None
        if type(another_list is LinkedList):
            current_node_another_list = another_list.head
            if self.list_length() is 0 or another_list.list_length() is 0:
                return LinkedList()
            # infinite while loop
            while self.list_length() is not 0 and another_list.list_length() is not 0:
                # if current_node_self is None and current_node_another_list is not None:
                #     while current_node_another_list is not None:
                #         mylist.add(current_node_another_list)
                #         current_node_another_list = current_node_another_list.next
                # if current_node_another_list is None and current_node_self is not None:
                #     while current_node_self is not None:
                #         mylist.add(current_node_self)
                #         current_node_self = current_node_self.next
                if current_node_self is not None and current_node_another_list is not None:
                    if current_node_self.id is not current_node_another_list.id:
                        while current_node_self.id < current_node_another_list.id:
                            mylist.add(current_node_self)
                            if current_node_self.next is not None:
                                current_node_self = current_node_self.next
                            elif current_node_self is None and current_node_another_list is not None:
                                while current_node_another_list is not None:
                                    mylist.add(current_node_another_list)
                                    current_node_another_list = current_node_another_list.next
                                    if current_node_another_list is None:
                                        return list
                            elif current_node_self is None and current_node_another_list is None:
                                return list
                        while current_node_self.id > current_node_another_list.id:
                            mylist.add(current_node_another_list)
                            if current_node_another_list.next is not None:
                                current_node_another_list = current_node_another_list.next
                            elif current_node_another_list.next is None and current_node_self is not None:
                                while current_node_self is not None:
                                    mylist.add(current_node_self)
                                    current_node_self = current_node_self.next
                            elif current_node_self is None and current_node_another_list is None:
                                return list
                    elif current_node_self.id is current_node_another_list.id:
                        mylist.add(current_node_self)
                        current_node_another_list = current_node_another_list.next
                        current_node_self = current_node_self.next
                elif current_node_self.next is None and current_node_another_list.next is None:
                    return list
            return list

        #     while self.list_length() is not 0 and another_list.list_length() is not 0:
        #         if current_node_self is None and current_node_another_list is not None:
        #             while current_node_another_list is not None:
        #                 mylist.add(current_node_another_list)
        #                 current_node_another_list = current_node_another_list.next
        #         elif current_node_another_list is None and current_node_self is not None:
        #             while current_node_self is not None:
        #                 mylist.add(current_node_self)
        #                 current_node_self = current_node_self.next
        #         elif current_node_self is not None and current_node_another_list is not None:
        #             if current_node_self.id is not current_node_another_list.id:
        #                 while current_node_self is not None:
        #                     if current_node_self.id < current_node_another_list.id:
        #                         mylist.add(current_node_self)
        #                         current_node_self = current_node_self.next
        #                 while current_node_self is not None:
        #                     if current_node_self.id > current_node_another_list.id:
        #                         mylist.add(current_node_another_list)
        #                         current_node_another_list = current_node_another_list.next
        #             elif current_node_self.id is current_node_another_list.id:
        #                 mylist.add(current_node_self)
        #                 current_node_another_list = current_node_another_list.next
        #                 current_node_self = current_node_self.next
        #         elif current_node_self.next is None and current_node_another_list.next is None:
        #             return list
        # return list

    def intersect_with_another_list(self, another_list):
        mylist = LinkedList()
        current_node_self = self.head
        current_node_another_list = None
        if type(another_list is LinkedList):
            current_node_another_list = another_list.head
            if self.list_length() is 0 or another_list.list_length() is 0:
                return LinkedList()
            while self.list_length() is not 0 and another_list.list_length() is not 0:
                if current_node_self.id is not current_node_another_list.id:
                    while current_node_self.id < current_node_another_list.id:
                        if current_node_self.next is not None:
                            current_node_self = current_node_self.next
                        else:
                            return mylist
                    while current_node_self.id > current_node_another_list.id:
                        if current_node_another_list.next is not None:
                            current_node_another_list = current_node_another_list.next
                        else:
                            return mylist
                elif current_node_self.id is current_node_another_list.id:
                    mylist.add(current_node_self)
                    if current_node_self.next is not None and current_node_another_list.next is not None:
                        current_node_another_list = current_node_another_list.next
                        current_node_self = current_node_self.next
                    else:
                        return mylist
        return list
