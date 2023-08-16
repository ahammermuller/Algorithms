class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE SELECTION_SORT METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################

    def selection_sort(self):
        # If the length of the linked list is less than 2, it's already sorted.
        if self.length < 2:
            return
        
        current = self.head # Start from the beginning of the list.
        while current is not None:
            min_node = current # Assume the current node has the minimum value initially.
            temp = current.next # Start searching for a smaller value from the next node.

            # Iterate through the remaining nodes to find the minimum node.
            while temp is not None:
                if temp.value < min_node.value:
                    min_node = temp # Update the minimum node if a smaller value is found.
                temp = temp.next # Move to the next node for comparison.
            
            # If the minimum node is not the current node, swap their values.
            if min_node != current:
                current.value, min_node.value = min_node.value, current.value
            
            current = current.next # Move to the next node for the next iteration.
        self.tail = current # Update the tail pointer after sorting

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

