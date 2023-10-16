from collections import deque


def predictPartyVictory(self, senate):
    """
    :param senate: A string representing the configuration of the Senate, where 'R' denotes Radiant and 'D' denotes Dire.
    :return: A string indicating the predicted winner, either 'Radiant' or 'Dire'.
    """
    n = len(senate)

    # Create deques for Radiant and Dire senators, initializing with their indices
    r = deque([i for i in range(n) if senate[i] == 'R'])
    d = deque([i for i in range(n) if senate[i] == 'D'])

    # Simulate the banning process until one party has no members left
    while r and d:
        # Dequeue the front senators from both parties
        r1, d1 = r.popleft(), d.popleft()

        # Compare their indices and enqueue the next senator based on the result
        if r1 < d1:
            r.append(n + r1)  # Enqueue a Radiant senator with an updated index
        else:
            d.append(n + d1)  # Enqueue a Dire senator with an updated index

    # Determine the winner based on which party still has members
    return 'Radiant' if r else 'Dire'
