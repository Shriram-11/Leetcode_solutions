class Solution(object):
    def findJudge(self, n, trust):
        """
        Finds the town judge in a town where:
        - The town judge trusts nobody.
        - Everybody (except for the town judge) trusts the town judge.
        - There is exactly one person that satisfies properties 1 and 2.

        :param n: int: The number of people in the town.
        :param trust: List[List[int]]: List of trust relationships, where trust[i] = [trustor, trustee]
                      represents that person labeled 'trustor' trusts person labeled 'trustee'.
        :return: int: The label of the town judge if found; otherwise, returns -1.
        """
        # Initialize arrays to keep track of the count of trusts (trust_given) and trusted by (trust_received).
        trust_given = [0] * (n + 1)  # Stores the count of trusts given by each person.
        trust_received = [0] * (n + 1)  # Stores the count of trusts received by each person.

        # Iterate through the trust relationships.
        for trustor, trustee in trust:
            # Increment trust counts.
            trust_given[trustor] += 1
            trust_received[trustee] += 1

        # Iterate through each person from 1 to n.
        for person in range(1, n + 1):
            # Check if the person trusts nobody (trust_given[person] == 0) and is trusted by everybody except themselves.
            if trust_given[person] == 0 and trust_received[person] == (n - 1):
                # Return the label of the town judge.
                return person

        # If no town judge is found, return -1.
        return -1
