import numpy as np

def load_centerpoints_from_npz(npz_file_path):
    """
    Load centerpoints and their corresponding class labels from an NPZ file.

    Args:
        npz_file_path (str): Path to the NPZ file containing the centerpoint data.

    Returns:
        dict: Dictionary containing centerpoints keyed by class labels.
    """
    # Load the NPZ file
    data = np.load(npz_file_path, allow_pickle=True)

    # Extract the classes and centerpoints arrays
    classes = data['classes']
    centerpoints = data['centerpoints']

    # Group centerpoints by class
    centerpoints_dict = {}
    for class_label, point in zip(classes, centerpoints):
        if class_label not in centerpoints_dict:
            centerpoints_dict[class_label] = []
        centerpoints_dict[class_label].append(tuple(point))

    return centerpoints_dict

def main():
    npz_file_path = 'centerpoints.npz'  # Replace with your .npz file path
    centerpoints_data = load_centerpoints_from_npz(npz_file_path)
    print(centerpoints_data[0][:10])

if __name__ == "__main__":
    main()