def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left_half = string[:mid]
    right_half = string[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left_half, right_half):
    result = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result += left_half[i:]
    result += right_half[j:]

    return "".join(result)


def is_anagram(first_string, second_string):
    first_sorted_string = merge_sort(first_string.lower())
    second_sorted_string = merge_sort(second_string.lower())

    if not first_sorted_string or not second_sorted_string:
        return (first_sorted_string, second_sorted_string, False)

    return (
        first_sorted_string,
        second_sorted_string,
        first_sorted_string == second_sorted_string,
    )
