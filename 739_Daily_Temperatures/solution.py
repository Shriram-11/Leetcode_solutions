class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        Function to calculate the number of days to wait for warmer temperatures.

        Parameters:
        temperatures : List[int]
            An array of integers representing daily temperatures.

        Returns:
        List[int]
            An array containing the number of days you have to wait after the ith day
            to get a warmer temperature. If there is no future day for which this is
            possible, it will contain 0 instead.
        """
        # Initialize an empty stack to store indices of temperatures for which
        # warmer temperatures haven't been found yet.
        not_found = []
        
        # Initialize an output array with all elements set to 0.
        output = [0] * len(temperatures)
        
        # Iterate through the temperatures list along with their indices.
        for idx, temp in enumerate(temperatures):
            # While the not_found stack is not empty and the temperature at
            # the index on top of the stack (latest added) is less than the current temperature.
            while not_found and temperatures[not_found[-1]] < temp:
                # Pop the index from the not_found stack.
                prev_idx = not_found.pop()
                # Calculate the number of days waited by subtracting the current index
                # from the popped index. Assign this value to the output at the popped index.
                output[prev_idx] = idx - prev_idx
            
            # Append the current index to the not_found stack.
            not_found.append(idx)
        
        # Return the output array.
        return output
