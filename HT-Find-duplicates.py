# WRITE FIND_DUPLICATES FUNCTION HERE #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################

def find_duplicates(nums):
    duplicates = []
    unique_elements = []

    for num in nums:
        if num in unique_elements and num not in duplicates:
            duplicates.append(num)
        else:
            unique_elements.append(num)
    return duplicates

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""