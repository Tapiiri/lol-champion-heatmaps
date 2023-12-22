import numpy as np

def load_and_combine_npz_bounding_boxes(npz_file_paths):
    """
    Load bounding boxes from multiple NPZ files and combine them into a single list.

    Args:
        npz_file_paths (list): List of strings, where each string is a path to an NPZ file.

    Returns:
        list: Combined list of bounding boxes from all NPZ files.
    """
    combined_bounding_boxes = []
    for file_path in npz_file_paths:
        with np.load(file_path, allow_pickle=True) as data:
            bounding_boxes = data['boxes']
            combined_bounding_boxes.extend(bounding_boxes)
    return combined_bounding_boxes

def main():
    # Example usage:
    npz_file_paths = ['D:/DeepLeague100K/clusters_cleaned/train/data_training_set_cluster_0.npz', 'D:/DeepLeague100K/clusters_cleaned/train/data_training_set_cluster_1.npz']  # Replace with your actual NPZ file paths
    combined_bounding_boxes = load_and_combine_npz_bounding_boxes(npz_file_paths)
    print(len(combined_bounding_boxes))


if __name__ == "__main__":
    main()

