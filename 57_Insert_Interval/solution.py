def insert(intervals, newInterval):
    """
    Inserts a new interval into a list of non-overlapping intervals, merging if necessary.

    :param intervals: List[List[int]] - A list of non-overlapping intervals sorted by start time.
    :param newInterval: List[int] - An interval to insert, represented as [start, end].
    :return: List[List[int]] - The list of intervals after insertion and merging, if applicable.
    """
    res = []
    i = 0
    n = len(intervals)
    l, r = newInterval[0], newInterval[1]

    # Add all intervals that come before the new interval
    while i < n and intervals[i][1] < l:
        res.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and r >= intervals[i][0]:
        l = min(l, intervals[i][0])
        r = max(r, intervals[i][1])
        i += 1

    # Add the merged interval
    res.append([l, r])

    # Add all remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1

    return res
