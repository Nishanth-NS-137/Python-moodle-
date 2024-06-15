def find_substring_index(s1, s2):
    """
    Checks if s2 is a substring of s1.
   
    Args:
        s1 (str): The main string.
        s2 (str): The substring to search for.
   
    Returns:
        int: Index of the first occurrence of s2 in s1, or -1 if not found.
    """
    for i in range(len(s1) - len(s2) + 1):
        if s1[i:i + len(s2)] == s2:
            return i
    return -1

# Example usage
s1 = input()
s2 = input()

result = find_substring_index(s1, s2)
print( result)
