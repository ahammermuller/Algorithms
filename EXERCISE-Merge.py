
## WRITE MERGE FUNCTION HERE ##
#                             #
#                             #
#                             #
#                             #
############################### 

def merge(list1,  list2):
    combined = []
    i = 0
    j = 0

    # Compare elements from both lists and add the smaller one to the combined list.
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    # If there are remaining elements in list1, add them to the combined list.
    while i < len(list1):
        combined.append(list1[i])
        i += 1
        
    # If there are remaining elements in list2, add them to the combined list.
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


# MERGE REQUIRES TWO SORTED LISTS:
print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
 """