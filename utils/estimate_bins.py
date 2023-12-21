from .find_minimum_distance import find_minimum_distance
from scipy.spatial import distance_matrix
import numpy as np


def estimate_bins(centerpoints, image_size):
    min_dist = find_minimum_distance(centerpoints)
    
    if min_dist is None:
        return 10  # Default value, adjust as necessary

    # Calculate the number of bins for each axis based on the minimum distance
    x_bins = int(image_size[0] / min_dist)
    y_bins = int(image_size[1] / min_dist)

    # Use the smaller of the two values to maintain aspect ratio
    num_bins = min(x_bins, y_bins)

    # Make sure the number of bins is not too high
    # max_bins = 100  # Set a reasonable maximum to prevent excessive binning
    # num_bins = min(num_bins, max_bins)

    return num_bins

def main():
    centerpoints = [(1,2), (2,3), (3,4), (4,5)]  # Replace with your actual list of centerpoints
    # Example usage:
    num_bins = estimate_bins(centerpoints, image_size=(1920, 1080))
    print("Estimated number of bins:", num_bins)

# Example usage:
if __name__ == "__main__":
    main()