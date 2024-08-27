from collections import defaultdict, deque

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        Computes the maximum probability of reaching the end_node from the start_node
        in a graph where each edge has a probability of success.

        :type n: int
            Number of nodes in the graph.
        :type edges: List[List[int]]
            List of edges where each edge is represented as [a, b].
        :type succProb: List[float]
            List of probabilities corresponding to each edge.
        :type start_node: int
            The starting node for the probability computation.
        :type end_node: int
            The target node for the probability computation.
        :rtype: float
            The maximum probability of reaching end_node from start_node.
        """
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])
        
        # Initialize probabilities with 0.0, and set the start_node's probability to 1.0
        prob = [0.0] * n
        prob[start_node] = 1.0
        
        # Use a queue for BFS (Breadth-First Search)
        q = deque([start_node])
        
        while q:
            curr = q.popleft()
            for nxt, p in graph[curr]:
                # Calculate the probability to reach 'nxt' through 'curr'
                if prob[curr] * p > prob[nxt]:
                    prob[nxt] = prob[curr] * p
                    q.append(nxt)
        
        # Return the maximum probability to reach the end_node
        return prob[end_node]
