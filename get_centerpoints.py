from utils.rotate_centerpoints import rotate_centerpoints
from utils.estimate_bins import estimate_bins
from utils.compute_zoom_limits import compute_zoom_limits
from utils.create_heatmap import create_heatmap
from utils.load_npz_bounding_boxes import load_npz_bounding_boxes
from utils.convert_to_centerpoints import convert_to_centerpoints
from utils.overlay_heatmap_on_map import overlay_heatmap_on_map
import argparse

def main():
    parser = argparse.ArgumentParser(description='Convert bounding boxes to centerpoints.')
    parser.add_argument('--path', type=str, required=True, help='Path to the NPZ file.')
    args = parser.parse_args()

    bounding_boxes = load_npz_bounding_boxes(args.path)
    centerpoints = convert_to_centerpoints(bounding_boxes)

    # Define the zoom range based on the concentration area
    zoom_range = compute_zoom_limits(centerpoints)
    image_size = (zoom_range[0][1], zoom_range[1][1])

    bin_estimate = estimate_bins(centerpoints, (zoom_range[0][1], zoom_range[1][1]))

    centerpoints = rotate_centerpoints(centerpoints, (image_size[0], image_size[1]))

    # Create and show the heatmap with increased resolution and zoomed range
    heatmap, _, _  = create_heatmap(centerpoints, image_size, bins=bin_estimate)

    map_image_path = "assets/2x_2dlevelminimap.png"

    extent = (zoom_range[0][0], zoom_range[0][1], zoom_range[1][0], zoom_range[1][1])

    overlay_heatmap_on_map(heatmap, map_image_path, extent)



if __name__ == "__main__":
    main()
