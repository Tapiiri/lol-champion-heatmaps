import numpy as np

def load_npz_bounding_boxes(npz_file_path):
    """
    Load bounding boxes from an NPZ file.

    Args:
        npz_file_path (str): Path to the NPZ file.

    Returns:
        list: List of bounding boxes.
    """
    npz_data = np.load(npz_file_path, allow_pickle=True)
    bounding_boxes = npz_data['boxes']
    return bounding_boxes
