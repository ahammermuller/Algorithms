# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################

def group_anagrams(strings):
    anagram_groups = {}

    for string in strings:
        # Sort the characters in the string to form a sorted key
        sorted_string = ''.join(sorted(string))

        # Check if the sorted key already exists in the dictionary
        if sorted_string in anagram_groups:
            # If the key exists, append the string to the corresponding group
            anagram_groups[sorted_string].append(string)
        else:
            # If the key does not exist, create a new group with the string
            anagram_groups[sorted_string] = [string]

    # Convert the dictionary values to a list of lists to get the final result
    result = list(anagram_groups.values())

    return result


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""