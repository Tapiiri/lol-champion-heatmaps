def compute_zoom_limits(centerpoints, padding_percentage=0.05):
    """
    Compute the limits for zooming into the area where all centerpoints are located.

    Args:
        centerpoints (list): List of centerpoints (x, y).
        padding_percentage (float): Percentage of padding to add to the limits.

    Returns:
        tuple: ((x_min, x_max), (y_min, y_max))
    """
    # Extract x and y coordinates
    x_coords = [point[0] for point in centerpoints]
    y_coords = [point[1] for point in centerpoints]

    # Find the bounds with padding
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)

    # Calculate padding
    x_padding = (x_max - x_min) * padding_percentage
    y_padding = (y_max - y_min) * padding_percentage

    # Apply padding
    x_min -= x_padding
    x_max += x_padding
    y_min -= y_padding
    y_max += y_padding

    # Ensure that the limits do not go out of the expected range, e.g., the image size
    # x_min = max(x_min, 0)
    # y_min = max(y_min, 0)
    # x_max = min(x_max, 280)  # Assuming 280 is the maximum value for x
    # y_max = min(y_max, 280)  # Assuming 280 is the maximum value for y

    return ((x_min, x_max), (y_min, y_max))

def main():
    centerpoints = [(1,2), (2,3), (3,4), (4,5)]  # Replace with your actual list of centerpoints
    # Example usage:
    zoom_limits = compute_zoom_limits(centerpoints)
    print("Computed zoom limits:", zoom_limits)


if __name__ == "__main__":
    main()