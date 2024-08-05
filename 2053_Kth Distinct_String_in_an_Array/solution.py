
def kthDistinct(arr, k):
    """
    Finds the k-th distinct string in the list `arr`.

    :type arr: List[str]   # List of strings to be searched.
    :type k: int           # The k-th distinct element to find.
    :rtype: str            # The k-th distinct string, or an empty string if not found.
    """
    # Step 1: Create a dictionary to count the occurrences of each element.
    d = {}
    for a in arr:
        if a in d:
            # Increment the count for this element if it already exists in the dictionary.
            d[a] += 1
        else:
            # Initialize the count for this new element in the dictionary.
            d[a] = 1
    
    # Step 2: Iterate over the list again to find the k-th distinct element.
    for a in arr:
        # Check if the current element is distinct (occurs exactly once).
        if d[a] == 1:
            # Decrease k as we found another distinct element.
            k -= 1
            # If k is zero, it means this is the k-th distinct element, so return it.
            if k == 0:
                return a
    
    # If we haven't found the k-th distinct element, return an empty string.
    return ""
