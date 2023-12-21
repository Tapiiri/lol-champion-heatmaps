import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter

def create_heatmap(centerpoints, image_size, bins=200, zoom_range=None):
    """
    Create a heatmap from centerpoints with higher resolution and zoom capability.

    Args:
        centerpoints (list): List of centerpoints (x, y).
        image_size (tuple): Size of the image (width, height).
        bins (int): Number of bins for the histogram.
        zoom_range (tuple): The zoom range for x and y coordinates ((x_min, x_max), (y_min, y_max)).

    Returns:
        None
    """
    x_points = [point[0] for point in centerpoints]
    y_points = [point[1] for point in centerpoints]

    # Determine the range for the histogram
    if zoom_range:
        hist_range = zoom_range
    else:
        hist_range = [[0, image_size[0]], [0, image_size[1]]]

    heatmap, xedges, yedges = np.histogram2d(x_points, y_points, bins=bins, range=hist_range)

    # Create an image
    plt.imshow(heatmap.T, origin='lower', cmap='hot', interpolation='nearest', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
    plt.colorbar()
    plt.title("Heatmap of Centerpoints")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    # # After creating the 2D histogram:
    # heatmap, xedges, yedges = np.histogram2d(x_points, y_points, bins=bins, range=hist_range)

    # # Apply a Gaussian filter to smooth the heatmap
    # smoothed_heatmap = gaussian_filter(heatmap, sigma=1)  # You can adjust the sigma value

    # # Then create an image using the smoothed heatmap
    # plt.imshow(smoothed_heatmap.T, origin='lower', cmap='hot', interpolation='nearest', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
    # plt.colorbar()

    plt.show()

    return heatmap, xedges, yedges

