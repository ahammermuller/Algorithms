## WRITE SELECTION_SORT FUNCTION HERE ##
#                                      #
#                                      #
#                                      #
#                                      #
######################################## 
    

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i  # Assume the current index has the smallest value initially.

        # Search for the smallest element from i+1 to the end of the list.
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j # Update the index of the smallest element found.

        # If the smallest element is not already at its correct position (i),
        # swap the elements at min_index and i to put the smallest element in place.
        if i!= min_index:
            my_list[min_index], my_list[i] = my_list[i], my_list[min_index]
    return my_list


print(selection_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

