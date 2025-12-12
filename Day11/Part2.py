from collections import defaultdict
import sys

# Increase the recursion limit for potentially deep paths
sys.setrecursionlimit(3000)

def count_constrained_paths(file_path):
    """
    Counts the number of paths from 'svr' to 'out' that must visit both 
    'dac' and 'fft' (in any order).
    """
    graph = defaultdict(list)
    
    try:
        # --- 1. Parse the Input File and Build the Graph ---
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    source = parts[0].strip()
                    targets = parts[1].strip().split()
                    graph[source].extend(targets)
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found. Please ensure it is in the same directory as the script."

    # --- 2. DFS Function with Memoization ---
    def count_paths(start_node, end_node, memo=None):
        """
        Calculates the number of distinct paths from start_node to end_node.
        This function is self-contained for memoization per segment calculation.
        """
        if memo is None:
            memo = {}
            
        def dfs(device):
            # Base Case 1: Target reached
            if device == end_node:
                return 1
            
            # Check Memoization Table
            if device in memo:
                return memo[device]

            # Base Case 2: Device is a dead-end for this segment
            if device not in graph:
                return 0

            # Recursive Step
            total_paths = 0
            for next_device in graph[device]:
                total_paths += dfs(next_device)

            # Store result in memo and return
            memo[device] = total_paths
            return total_paths
        
        return dfs(start_node)

    # Define the required nodes
    START_NODE = 'svr'
    END_NODE = 'out'
    NODE_A = 'dac'
    NODE_B = 'fft'

    # --- 3. Calculate Paths for Scenario 1: SVR -> A -> B -> OUT (dac -> fft) ---
    # Path is SVR -> DAC -> FFT -> OUT
    
    # Segment 1: SVR to DAC
    paths_svr_to_a = count_paths(START_NODE, NODE_A)
    # Segment 2: DAC to FFT
    paths_a_to_b = count_paths(NODE_A, NODE_B)
    # Segment 3: FFT to OUT
    paths_b_to_out = count_paths(NODE_B, END_NODE)
    
    # Total paths for Scenario 1: Product of segments
    scenario_1_paths = paths_svr_to_a * paths_a_to_b * paths_b_to_out

    # --- 4. Calculate Paths for Scenario 2: SVR -> B -> A -> OUT (fft -> dac) ---
    # Path is SVR -> FFT -> DAC -> OUT
    
    # Segment 1: SVR to FFT
    paths_svr_to_b = count_paths(START_NODE, NODE_B)
    # Segment 2: FFT to DAC
    paths_b_to_a = count_paths(NODE_B, NODE_A)
    # Segment 3: DAC to OUT
    paths_a_to_out = count_paths(NODE_A, END_NODE)
    
    # Total paths for Scenario 2: Product of segments
    scenario_2_paths = paths_svr_to_b * paths_b_to_a * paths_a_to_out

    # --- 5. Total Paths ---
    total_constrained_paths = scenario_1_paths + scenario_2_paths
    
    return total_constrained_paths

# --- Main execution block ---
FILE_NAME = 'data.txt'
path_count = count_constrained_paths(FILE_NAME)

if isinstance(path_count, int):
    print(f"The number of paths from 'svr' to 'out' that visit both 'dac' and 'fft' is: {path_count}")
else:
    # Prints the error message if the file was not found
    print(path_count)