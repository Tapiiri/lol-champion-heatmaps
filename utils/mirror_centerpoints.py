def mirror_centerpoints(centerpoints, max_values):
    """
    Mirror the centerpoints along the x-axis.

    Args:
        centerpoints (list): List of centerpoints (x, y).
        max_values (int, int): The width and the height of the plot area or the real-life situation.

    Returns:
        list: List of mirrored centerpoints.
    """
    max_x_value, max_y_value = max_values

    mirrored_centerpoints = [((max_x_value - x), (max_y_value - y)) for x, y in centerpoints]
    return mirrored_centerpoints

def main():
    centerpoints = [(1,2), (2,3), (3,4), (4,5)]  # Replace with your actual list of centerpoints
    # Example usage:
    max_x_value = 280  # Replace with the actual width of your plot area
    mirrored_centerpoints = mirror_centerpoints(centerpoints, max_x_value)
    print(mirrored_centerpoints)

# Example usage:
if __name__ == "__main__":
    main()