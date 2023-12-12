
def sum_two(nums: list[int], target: int) -> list[int]:
    """Return indices of the two numbers such that they add up to target.

    Args:
        nums (list[int]): List of integers.
        target (int): Target integer.

    Returns:
        list[int]: List of indices of the two numbers such that they add up to target.

    Examples:
        >>> sum_two([2, 7, 11, 15], 9)
        [0, 1]
        >>> sum_two([3, 2, 4], 6)
        [1, 2]
        >>> sum_two([3, 3], 6)
        [0, 1]
    """
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(sum_two([2, 7, 11, 15], 9))
    print(sum_two([3, 2, 4], 6))
    print(sum_two([3, 3], 6))

# Output:
# [0, 1]
# [1, 2]
# [0, 1]
