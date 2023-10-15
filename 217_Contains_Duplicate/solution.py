'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''


def duplicate(arr):
    # create an empty set
    s = set()
    # traverse each element if the elelemt is present in set return True else add the element to the set
    for a in arr:
        if a in s:
            return True
        s.add(a)
    return False
