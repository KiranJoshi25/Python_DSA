'''
node class
'''
class Node():

    def __init__(self,data):
        '''
        default constructor for Node class
        :param data:
        '''
        self.data = data
        self.next = None

'''
LinkedList Implementation
'''
class LinkedList():

    def __init__(self):
        self.head = None
        self.number_of_nodes = 0


    def insert_node(self,data):

        if not self.head:
            self.head = Node(data)
            self.number_of_nodes += 1

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data)
            self.number_of_nodes += 1

    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="=>")
            current_node = current_node.next

    def get_number_of_nodes_in_list(self):
        return self.number_of_nodes

    def delete_head_node(self):

        current_node = self.head
        current_node = current_node.next
        self.head = current_node
        self.number_of_nodes -= 1



List = [1,2,3]
L = LinkedList()
for i in List:
    L.insert_node(i)
L.delete_head_node()
L.print_linked_list()
