from collections import defaultdict, Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))

        # Union-Find helper functions
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # 1. Group indices into connected components
        for a, b in allowedSwaps:
            union(a, b)

        # 2. Map indices to their components
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)

        total_matches = 0

        # 3. For each component, count how many source elements can match target elements
        for indices in components.values():
            source_vals = Counter(source[i] for i in indices)
            for i in indices:
                if source_vals[target[i]] > 0:
                    total_matches += 1
                    source_vals[target[i]] -= 1
        
        # Hamming distance is total elements minus the ones we could match
        return n - total_matches