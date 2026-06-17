

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Step 1: Build the adjacency list graph
        # graph[u] = [(v, price), ...]
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
            
        # Step 2: Initialize Min-Heap 
        # Priority Queue stores: (cost, current_node, stops_remaining)
        # We start at 'src' with cost 0 and k + 1 allowed edge transitions (k stops + 1 final flight)
        min_heap = [(0, src, k + 1)]
        
        # Array to store the maximum remaining stops encountered for each node.
        # This helps prune paths that explore a node with fewer stops remaining than a previous path.
        stops_recorded = [-1] * n
        
        # Step 3: Process the graph
        while min_heap:
            cost, u, stops_left = heapq.heappop(min_heap)
            
            # If we reached the destination, this is guaranteed to be the cheapest valid path
            if u == dst:
                return cost
                
            # If we have no flight moves left, we cannot move further from this node
            if stops_left == 0:
                continue
                
            # Optimization: If we've already visited this node with a path that left 
            # more (or equal) stops remaining, skip exploring this worse path.
            if stops_recorded[u] >= stops_left:
                continue
            
            # Record the stops left for this node
            stops_recorded[u] = stops_left
            
            # Explore neighbors
            for neighbor, price in graph[u]:
                heapq.heappush(min_heap, (cost + price, neighbor, stops_left - 1))
                
        return -1