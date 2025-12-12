from collections import defaultdict
import sys

# Increase the recursion limit for potentially deep paths in the graph
sys.setrecursionlimit(3000)

def count_paths_from_start_to_end(file_path):
    """
    Counts the number of distinct paths from the 'you' device to the 'out' device
    in a network of connections, using DFS with memoization (dynamic programming).
    
    Args:
        file_path (str): The name of the file containing the device connections.
        
    Returns:
        int: The total number of paths, or an error message string.
    """
    graph = defaultdict(list)
    
    try:
        # --- 1. Parse the Input File and Build the Graph ---
        with open(file_path, 'r') as f:
            for line in f:
                # Example line format: aaa: you hhh
                parts = line.strip().split(':')
                if len(parts) == 2:
                    source = parts[0].strip()
                    # Split the targets by space
                    targets = parts[1].strip().split() 
                    graph[source].extend(targets)
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found. Please ensure it is in the same directory as the script."

    memo = {}  # Memoization table to store results: {device: path_count_to_out}
    START_DEVICE = 'you'
    TARGET_DEVICE = 'out'

    # --- 2. DFS Function with Memoization ---
    def count_paths(device):
        """
        Recursive function to count paths from a given 'device' to the 'out' device.
        """
        # Base Case 1: Target reached
        if device == TARGET_DEVICE:
            return 1
        
        # Check Memoization Table
        if device in memo:
            return memo[device]

        # Base Case 2: Device is a dead-end (not in graph, and not the target)
        if device not in graph:
            # We don't need to memoize dead ends unless they were explicitly 
            # defined with no outputs, but for safety, we can return 0.
            return 0

        # Recursive Step: Sum the paths from all connected devices
        total_paths = 0
        for next_device in graph[device]:
            total_paths += count_paths(next_device)

        # Store result in memo and return
        memo[device] = total_paths
        return total_paths

    # --- 3. Start the Counting ---
    result = count_paths(START_DEVICE)
    
    return result

# --- Main execution block ---
FILE_NAME = 'data.txt'
path_count = count_paths_from_start_to_end(FILE_NAME)

if isinstance(path_count, int):
    print(f"The number of different paths from '{'you'}' to '{'out'}' is: {path_count}")
else:
    # Prints the error message if the file was not found
    print(path_count)