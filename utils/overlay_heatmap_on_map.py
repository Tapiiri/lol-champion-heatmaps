import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from .mirror_centerpoints import mirror_centerpoints
from .estimate_bins import estimate_bins
from .compute_zoom_limits import compute_zoom_limits
from .create_heatmap import create_heatmap


def overlay_heatmap_on_map(heatmap_data, map_image_path, extent, alpha=0.8):
    """
    Overlay a heatmap on a map image.

    Args:
        heatmap_data (numpy.ndarray): The 2D array of the heatmap data.
        map_image_path (str): The file path to the map image.
        extent (tuple): The (left, right, bottom, top) range of the heatmap data.
        alpha (float): The transparency level of the heatmap.

    Returns:
        None: The function displays the plot.
    """
    # Load the map image
    map_img = mpimg.imread(map_image_path)

    # Plot the map
    plt.imshow(map_img, extent=extent)

    # Overlay the heatmap
    plt.imshow(heatmap_data, origin='lower', cmap='hot', interpolation='nearest', alpha=alpha, extent=extent)

    # Add the colorbar and other plot components
    plt.colorbar()
    plt.grid(False)  # Turn off the grid if needed
    plt.axis('on')  # Turn off the axis if needed
    plt.show()

def main():
    centerpoints = [(1,2), (2,3), (3,4), (4,5)]  # Replace with your actual list of centerpoints
    # Define the zoom range based on the concentration area
    zoom_range = compute_zoom_limits(centerpoints)
    image_size = (zoom_range[0][1], zoom_range[1][1])

    bin_estimate = estimate_bins(centerpoints, (zoom_range[0][1], zoom_range[1][1]))

    centerpoints = mirror_centerpoints(centerpoints, image_size[0])

    # Create and show the heatmap with increased resolution and zoomed range
    heatmap = create_heatmap(centerpoints, image_size, bins=bin_estimate)
    # Example usage:
    # Assuming 'heatmap' is your 2D numpy array with heatmap data
    # and 'extent' is the range of your heatmap data that matches the map image.
    map_image_path = 'assets/2x_2dlevelminimap.png'
    extent = (zoom_range[0][0], zoom_range[0][1], zoom_range[1][0], zoom_range[1][1])
    overlay_heatmap_on_map(heatmap, map_image_path, extent)

if __name__ == "__main__":
    main()