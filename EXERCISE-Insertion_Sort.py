## WRITE INSERTION_SORT FUNCTION HERE ##
#                                      #
#                                      #
#                                      #
#                                      #
######################################## 

def insertion_sort(my_list):
    for i in range (1, len(my_list)):
        temp = my_list[i] # Store the current element in a temporary variable.
        j = i-1 # Initialize a variable to move through the sorted portion of the list.

        # While the current element is smaller than the element to its left, and we haven't reached the beginning:
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]  # Shift the larger element to the right.
            my_list[j] = temp # Place the current element in its correct sorted position.
            j -= 1 # Move left to compare with the previous element.
            
    return my_list



print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

