import numpy as np
import argparse
import os
from utils.convert_to_centerpoints import convert_to_centerpoints
from utils.get_npz_file_paths import get_npz_file_paths
from utils.load_and_combine_npz_bounding_boxes import load_and_combine_npz_bounding_boxes

def save_centerpoints_as_npz(centerpoints_dict, output_file):
    """
    Save the centerpoints and their corresponding class labels as an NPZ file.

    Args:
        centerpoints_dict (dict): Dictionary containing centerpoints keyed by class labels.
        output_file (str): Path to the output NPZ file.
    """
    # Flatten the dictionary into lists of classes and centerpoints
    classes = []
    points = []
    for class_label, centerpoints in centerpoints_dict.items():
        for point in centerpoints:
            classes.append(class_label)
            points.append(point)

    # Convert lists to numpy arrays
    classes_array = np.array(classes)
    points_array = np.array(points)

    # Save the arrays as an NPZ file
    np.savez(output_file, classes=classes_array, centerpoints=points_array)
    print(f"Saved {len(points)} centerpoints to {output_file}")
    print(points[:20])

def main():
    parser = argparse.ArgumentParser(description='Overlay heatmap on map and save as an image.')
    parser.add_argument('-o', '--output-path', type=str, default='output.npz',
                        help='Optional: Output folder for the saved heatmap image. Defaults to "output".')
    parser.add_argument('-f', '--file-names', nargs='+', help='List of NPZ filenames or a file containing NPZ filenames')
    parser.add_argument('-c', '--class-names', type=str, help='List of NPZ class names in sequential order (eq. first class name is for class 0)')
    args = parser.parse_args()

    file_names = args.file_names
    npz_file_paths = get_npz_file_paths(file_names)
     
    bounding_boxes_with_labels = load_and_combine_npz_bounding_boxes(npz_file_paths)
    centerpoints_dict = convert_to_centerpoints(bounding_boxes_with_labels)

    save_centerpoints_as_npz(centerpoints_dict, args.output_path)


if __name__ == "__main__":
    main()
