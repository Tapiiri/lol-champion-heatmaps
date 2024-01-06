from collections import defaultdict

def convert_to_centerpoints(farsight_json_data):
    """
    Convert bounding boxes to centerpoints.

    Args:
        bounding_boxes (list): List of bounding boxes.

    Returns:
        list: List of centerpoints.
    """
    centerpoints_dict = defaultdict(list)
     # Filter and combine the data
    for item in farsight_json_data:
        class_label, x_coord, y_coord, timestamp, is_alive = item
        if is_alive:  # Only include alive points
            centerpoints_dict[class_label].append((x_coord, y_coord))

    return centerpoints_dict
