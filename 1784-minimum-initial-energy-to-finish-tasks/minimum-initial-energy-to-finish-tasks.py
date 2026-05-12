class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        # Sort by the gap between requirement and cost (descending)
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        total_initial_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            if current_energy < minimum:
                # Calculate how much more starting energy we needed
                extra = minimum - current_energy
                total_initial_energy += extra
                current_energy = minimum
            
            # Spend the energy
            current_energy -= actual
            
        return total_initial_energy
        