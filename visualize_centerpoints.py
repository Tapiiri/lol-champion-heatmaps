from utils.rotate_centerpoints import rotate_centerpoints
from utils.estimate_bins import estimate_bins
from utils.compute_zoom_limits import compute_zoom_limits
from utils.create_heatmap import create_heatmap
from utils.convert_to_centerpoints import convert_to_centerpoints
from utils.overlay_heatmap_on_map import overlay_heatmap_on_map
from utils.get_npz_file_paths import get_npz_file_paths
from utils.load_and_combine_npz_bounding_boxes import load_and_combine_npz_bounding_boxes
import argparse
import os

def visualize_centerpoints(file_names, output_folder):
    bounding_boxes_with_labels = load_and_combine_npz_bounding_boxes(file_names)
    centerpoints_with_labels = convert_to_centerpoints(bounding_boxes_with_labels)
    centerpoints = [(point[1], point[2]) for point in centerpoints_with_labels]

    # Define the zoom range based on the concentration area
    zoom_range = compute_zoom_limits(centerpoints)
    image_size = (zoom_range[0][1], zoom_range[1][1])

    bin_estimate = estimate_bins(centerpoints, (zoom_range[0][1], zoom_range[1][1]))

    centerpoints = rotate_centerpoints(centerpoints, (image_size[0], image_size[1]))

    # Create and show the heatmap with increased resolution and zoomed range
    heatmap, _, _  = create_heatmap(centerpoints, image_size, bins=bin_estimate, show = False)

    map_image_path = "assets/2x_2dlevelminimap.png"

    extent = (zoom_range[0][0], zoom_range[0][1], zoom_range[1][0], zoom_range[1][1])

    output_path = os.path.join(output_folder, 'heatmap_overlay.png')

    overlay_heatmap_on_map(heatmap, map_image_path, extent, output_path, save = True, show = False)


def main():
    parser = argparse.ArgumentParser(description='Overlay heatmap on map and save as an image.')
    parser.add_argument('-o', '--output-folder', type=str, default='output',
                        help='Optional: Output folder for the saved heatmap image. Defaults to "output".')
    parser.add_argument('-f', '--file-names', nargs='+', help='List of NPZ filenames or a file containing NPZ filenames')
    args = parser.parse_args()

    output_folder = args.output_folder

    # Check if the output folder exists, and create it if it doesn't
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)

    file_names = args.file_names
    npz_file_paths = get_npz_file_paths(file_names)
     
    visualize_centerpoints(npz_file_paths, output_folder)


if __name__ == "__main__":
    main()
