# 1. Two Sum

Given an array of integers `nums` and an integer `target`, return *indices of the
two numbers such that they add up to `target`.*

You may assume that each input would **have exactly one solution**,
and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**

```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**

* $2 <= nums.length <= 10^4$
* $-10^9 <= nums[i] <= 10^9$
* $-10^9 <= target <= 10^9$
* Only one valid answer exists.

## Solutions

### Approach 1: Brute Force

We can loop through each element `x`, and find if there is another value that
the sum of `x` and that value equals to `target`. As we need to loop through
each element, the time complexity is $O(n^2)$.

See [two_sum_brute_force.py](./two_sum_brute_force.py).

### Approach 2: Two-pass Hash Table

To improve our run time complexity, we need a more efficient way to check if
the complement exists in the array. To know the complement of `x`, we can
calculate `target - x`.

See [two_sum_two_pass_hash_table.py](./two_sum_hash_table.py).
