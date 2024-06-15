def count_words_of_min_length(S, L):
    # Split the string into words using whitespace as the delimiter
    words = S.split()

    # Initialize a counter for valid words
    valid_word_count = 0

    # Check each word's length and count if it meets the minimum length requirement
    for word in words:
        # Remove any punctuation marks from the word
        cleaned_word = ''.join(c for c in word if c.isalnum())
        if len(cleaned_word) >= L:
            valid_word_count += 1

    return valid_word_count

# Example usage
S = input().strip()  # Read the input string
L = int(input().strip())  # Read the minimum word length

result = count_words_of_min_length(S, L)
print(result)
