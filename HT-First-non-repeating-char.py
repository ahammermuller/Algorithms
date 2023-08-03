# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################

def first_non_repeating_char(string):
    repeated_chars = [] 
    for char in string:
        if char in repeated_chars:
            continue
        if string.count(char) > 1:
            repeated_chars.append(char)
        else:
            return char

    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""