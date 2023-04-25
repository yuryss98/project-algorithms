def is_palindrome_iterative(word):
    if not word:
        return False

    high_index = len(word) - 1
    for letter in word:
        if letter != word[high_index]:
            return False

        high_index -= 1

    return True
