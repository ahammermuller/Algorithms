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

    # WRITE BUBBLE_SORT METHOD HERE #
    #                               #
    #                               #
    #                               #
    #                               #
    #################################

    def bubble_sort(self):
        # If the length of the linked list is less than or equal to 1, it's already sorted.
        if self.length < 2:
            return
        
        swapped = True # Flag to track if any swaps were made in the current pass.
        while swapped:
            swapped = False # Reset the swap flag for each pass.
            current = self.head # Start from the beginning of the list.

            # Iterate through the linked list until the second-to-last element.
            while current.next is not None:
                
                # Compare the current element with the next element.
                if current.value > current.next.value:
                    # Swap the values of the current element and the next element.
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True # Set the swap flag since a swap occurred.
                current = current.next # Move to the next element for comparison.
        


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

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

