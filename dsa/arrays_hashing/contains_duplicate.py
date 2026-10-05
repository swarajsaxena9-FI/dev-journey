"""
Problem: Contains Duplicate
Signal → Pattern: "kya koi value dobara aayi?" → seen-set (hashing)
Brute force: har pair compare, O(n^2)
Optimal: set mein daalte jao, pehle se hai to True. O(n) time, O(n) space
Khud se hua? haan
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
