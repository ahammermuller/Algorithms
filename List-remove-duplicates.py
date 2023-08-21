# WRITE REMOVE_DUPLICATES FUNCTION HERE #
#                                       #
#                                       #
#                                       #
#                                       #
#########################################
    
def remove_duplicates(nums):
    # If the input list is empty, there are no duplicates to remove
    if not nums:
        return 0
    
    # Initialize an index to keep track of the last unique element found
    unique_index = 0
    
    # Loop through the list starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous unique element
        if nums[i] != nums[unique_index]:
            # Move the unique index forward
            unique_index += 1
            # Update the element at the unique index to the current element
            nums[unique_index] = nums[i]
    
    # Return the new length of the modified list (number of unique elements)
    return unique_index + 1    

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])


"""
    EXPECTED OUTPUT:
    ----------------
    New length: 5
    Unique values in list: [0, 1, 2, 3, 4]

"""