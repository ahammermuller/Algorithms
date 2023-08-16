## WRITE BUBBLE_SORT FUNCTION HERE ##
#                                   #
#                                   #
#                                   #
#                                   #
##################################### 
    

def bubble_sort(my_list):
    # len(my_list) - 1: This represents the starting point of the range. It's the length of the list minus 1 because indexing in Python starts from 0. 
    # So, if my_list has a length of 5, len(my_list) - 1 would be 4, which is the index of the last element in the list.

    # 0: This is the ending point of the range. The loop will stop just before reaching the value 0. In other words, it will run until the index 0 is included.

    # -1: This is the step value. It indicates that the loop will decrement the index by 1 in each iteration. This causes the loop to iterate in reverse order.
    
    for i in range (len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list



print(bubble_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """