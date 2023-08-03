# WRITE TWO_SUM FUNCTION HERE #
#                             #
#                             #
#                             #
#                             #
###############################
    
def two_sum(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        # Check if the complement is already in the dictionary
        if complement in num_dict:
            # If yes, return the indices of the current number and its complement
            return [num_dict[complement], i]
        else:
            # If not, add the current number and its index to the dictionary
            num_dict[num] = i

    # If no two numbers add up to the target, return an empty list
    return []    
    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""