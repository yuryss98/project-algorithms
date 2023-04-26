def find_duplicate(nums):
    if not nums or len(nums) < 2:
        return False

    nums_set = set()
    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False
        if number in nums_set:
            return number
        nums_set.add(number)

    return False
