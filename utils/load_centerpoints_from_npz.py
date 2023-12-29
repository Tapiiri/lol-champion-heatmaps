import numpy as np

def load_centerpoints_from_npz(npz_file_paths):
    """
    Load centerpoints and their corresponding class labels from an NPZ file.

    Args:
        npz_file_path (list): List of paths to the NPZ files containing the centerpoint data.

    Returns:
        dict: Dictionary containing centerpoints keyed by class labels.
    """
    centerpoints_dict = {}

    # Load the NPZ files
    for file_path in npz_file_paths:
        with np.load(file_path, allow_pickle=True) as data:
            # Extract the classes and centerpoints arrays
            classes = data['classes']
            centerpoints = data['centerpoints']

            # Group centerpoints by class
            for class_label, point in zip(classes, centerpoints):
                if class_label not in centerpoints_dict:
                    centerpoints_dict[class_label] = []
                centerpoints_dict[class_label].append(tuple(point))

    return centerpoints_dict

def main():
    npz_file_paths = ['data/centerpoints.npz']  # Replace with your .npz file path
    centerpoints_data = load_centerpoints_from_npz(npz_file_paths)
    print(centerpoints_data[0][:10])

if __name__ == "__main__":
    main()