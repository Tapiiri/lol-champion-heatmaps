import numpy as np

def find_minimum_distance(centerpoints):
    """
    Finds the approximate minimum non-zero distance between centerpoints by sorting and comparing only neighbors.

    Args:
        centerpoints (list): List of centerpoints (x, y).

    Returns:
        float: The approximate minimum non-zero distance between centerpoints.
    """
    if len(centerpoints) < 2:
        # Not enough points to calculate distance
        return None
    
    # Sort the points by x, then y
    sorted_points = sorted(centerpoints, key=lambda point: (point[0], point[1]))
    
    # Calculate distances between adjacent points
    min_dist = float('inf')
    for i in range(len(sorted_points) - 1):
        point = sorted_points[i]
        next_point = sorted_points[i + 1]
        
        # Use Euclidean distance
        dist = np.hypot(next_point[0] - point[0], next_point[1] - point[1])
        if dist > 0:
            min_dist = min(min_dist, dist)
    
    if min_dist == float('inf'):
        # If all points are the same, min_dist wasn't updated
        return 0
    return min_dist

def main():
    centerpoints = [(1,2), (2,3), (3,4), (4,5)]  # Replace with your actual list of centerpoints
    min_distance = find_minimum_distance(centerpoints)
    print("Minimum non-zero distance between centerpoints:", min_distance)

# Example usage:
if __name__ == "__main__":
    main()
