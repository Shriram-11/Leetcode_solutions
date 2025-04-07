import heapq

def totalCost(costs, k, candidates):
    """
    Calculates the total cost to hire exactly k workers from a list of costs, while following the hiring rules.

    In each hiring session, we select the worker with the smallest cost from either the first 'candidates' workers
    or the last 'candidates' workers. If the costs are equal, the worker with the smallest index is selected.

    Args:
        costs (List[int]): A list where each element represents the cost of hiring a worker.
        k (int): The number of workers to hire.
        candidates (int): The number of workers to consider from both the start and end of the costs list.

    Returns:
        int: The total cost of hiring exactly k workers.

    Example:
        costs = [3, 2, 7, 7, 1, 2]
        k = 3
        candidates = 2
        totalCost(costs, k, candidates) -> 8
    """
    
    # Initialize two heaps: one for the first 'candidates' workers and one for the last 'candidates' workers
    first = costs[:candidates]
    last = costs[max(candidates, len(costs) - candidates):]
    
    # Convert both lists into heaps
    heapq.heapify(first)
    heapq.heapify(last)
    
    cost = 0
    next_first, next_last = candidates, len(costs) - candidates - 1
    
    for _ in range(k):
        # Determine which heap to pop from based on the smallest cost
        if not last or (first and first[0] <= last[0]):
            cost += heapq.heappop(first)
            # Add the next worker from the remaining candidates to the 'first' heap
            if next_first <= next_last:
                heapq.heappush(first, costs[next_first])
                next_first += 1
        else:
            cost += heapq.heappop(last)
            # Add the next worker from the remaining candidates to the 'last' heap
            if next_first <= next_last:
                heapq.heappush(last, costs[next_last])
                next_last -= 1
    
    return cost
