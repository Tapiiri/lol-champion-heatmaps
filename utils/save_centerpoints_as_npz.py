import numpy as np

from typedefs.centerpoint import Centerpoint

def save_centerpoints_as_npz(centerpoints_dict, output_file):
    """
    Save the centerpoints and their corresponding class labels as an NPZ file.

    Args:
        centerpoints_dict (dict): Dictionary containing centerpoints keyed by class labels.
        output_file (str): Path to the output NPZ file.
    """
    # Flatten the dictionary into lists of classes and centerpoints
    gameIds = []
    teamIds = []
    classes = []
    timestamps = []
    points = []
    healths = []

    is_old_centerpoint_type = "timestamp" not in list(centerpoints_dict.values())[0][0].keys()
    print(list(centerpoints_dict.values())[0][0].keys())

    if is_old_centerpoint_type:
        centerpoints_dict = {k: v["point"] for k, v in centerpoints_dict.items()}
        for class_label, centerpoints in centerpoints_dict.items():
            for point in centerpoints:
                classes.append(class_label)
                points.append(point)
    else:
        for class_label, centerpoints in centerpoints_dict.items():
            for point in centerpoints:
                gameIds.append(point["gameid"])
                teamIds.append(point["teamid"])
                classes.append(point["classid"])
                timestamps.append(point["timestamp"])
                points.append(point["point"])
                healths.append(point["health"])

    # Convert lists to numpy arrays
    gameIds_array, teamIds_array, classes_array, timestamps_array, points_array, healths_array = [np.array(x) for x in [gameIds, teamIds, classes, timestamps, points, healths]]
    

    # Save the arrays as an NPZ file
    np.savez(output_file, classes=classes_array, centerpoints=points_array, timestamps=timestamps_array, healths=healths_array, gameIds=gameIds_array, teamIds=teamIds_array)
    print(f"Saved {len(points)} centerpoints to {output_file}")
    print(points[:20])
