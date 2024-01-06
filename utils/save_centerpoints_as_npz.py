import numpy as np

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
