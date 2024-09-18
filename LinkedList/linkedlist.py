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

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data)
    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="=>")
            current_node = current_node.next

List = [1,2,3]
L = LinkedList()
for i in List:
    L.insert_node(i)
L.print_linked_list()