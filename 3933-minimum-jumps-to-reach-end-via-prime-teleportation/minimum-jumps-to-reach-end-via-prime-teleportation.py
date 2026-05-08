import collections

class Solution(object):
    def minJumps(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        
        max_val = max(nums)
        # 1. Sieve to find Smallest Prime Factor (SPF) for factorization
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # 2. Map prime factors to indices where nums[j] % p == 0
        prime_to_indices = collections.defaultdict(list)
        for i, val in enumerate(nums):
            temp = val
            while temp > 1:
                p = spf[temp]
                prime_to_indices[p].append(i)
                while temp % p == 0:
                    temp //= p
        
        # 3. BFS
        queue = collections.deque([(0, 0)]) # (index, distance)
        visited_indices = {0}
        visited_primes = set()
        
        # Pre-check if index i is prime to enable teleportation
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_val**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, max_val + 1, i):
                    is_prime[j] = False

        while queue:
            curr_idx, dist = queue.popleft()
            
            if curr_idx == n - 1:
                return dist
            
            # --- Adjacent Steps ---
            for next_idx in [curr_idx - 1, curr_idx + 1]:
                if 0 <= next_idx < n and next_idx not in visited_indices:
                    if next_idx == n - 1: return dist + 1
                    visited_indices.add(next_idx)
                    queue.append((next_idx, dist + 1))
            
            # --- Prime Teleportation ---
            val = nums[curr_idx]
            if is_prime[val]:
                p = val
                if p not in visited_primes:
                    for next_idx in prime_to_indices[p]:
                        if next_idx not in visited_indices:
                            if next_idx == n - 1: return dist + 1
                            visited_indices.add(next_idx)
                            queue.append((next_idx, dist + 1))
                    # Optimization: Clear the list to avoid re-scanning
                    visited_primes.add(p)
                    del prime_to_indices[p]
        
        return -1
        