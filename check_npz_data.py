import numpy as np
import argparse

def load_npz_bounding_boxes(npz_file_path):
    """
    Load bounding boxes from an NPZ file.

    Args:
        npz_file_path (str): Path to the NPZ file.

    Returns:
        list: List of bounding boxes.
    """
    # Load the NPZ file
    npz_data = np.load(npz_file_path, allow_pickle=True)

    # Extract bounding boxes
    bounding_boxes = npz_data['boxes']

    print(npz_data)

    return bounding_boxes

def print_bounding_boxes(bounding_boxes):
    """
    Print the bounding boxes.

    Args:
        bounding_boxes (list): List of bounding boxes.
    """
    for i, box in enumerate(bounding_boxes):
        print(f"Bounding Box {i}: {box}")

def check_bounding_box_sizes(bounding_boxes, tolerance=0.05):
    if len(bounding_boxes) == 0 or len(bounding_boxes[0]) == 0:
        return True  # No boxes to check

    # Take the first bounding box from the first set of boxes
    first_box = bounding_boxes[0][0]
    first_width = first_box[3] - first_box[1]  # x_max - x_min
    first_height = first_box[4] - first_box[2]  # y_max - y_min

    if first_width == 0 or first_height == 0:
        print("Warning: First bounding box has zero width or height.")
        return False

    for boxes in bounding_boxes:
        for box in boxes:
            width = box[3] - box[1]
            height = box[4] - box[2]

            if width == 0 or height == 0:
                print("Warning: Bounding box has zero width or height.")
                continue

            width_diff = abs(width - first_width) / float(first_width)
            height_diff = abs(height - first_height) / float(first_height)

            if width_diff > tolerance or height_diff > tolerance:
                return (False, width_diff, height_diff)

    return (True, width_diff, height_diff)

# Example usage in your main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Load and display bounding boxes from NPZ file.')
    parser.add_argument('--path', type=str, required=True, help='Path to the NPZ file.')
    
    args = parser.parse_args()

    # Load bounding boxes from the specified NPZ file
    bounding_boxes = load_npz_bounding_boxes(args.path)

    check_results = check_bounding_box_sizes(bounding_boxes)

    # Check if bounding boxes have sizes within tolerance
    if check_results[0]:
        print(f"All bounding boxes sizes are within tolerance - width diff {check_results[1]}, height diff {check_results[2]}.")
    else:
        print(f"Bounding boxes sizes are not consistent with the first box - width diff {check_results[1]}, height diff {check_results[2]}.")
