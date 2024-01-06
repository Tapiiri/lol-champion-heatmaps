from collections import defaultdict

def convert_to_centerpoints(farsight_json_data):
    """
    Convert bounding boxes to centerpoints.

    Args:
        bounding_boxes (list): List of bounding boxes.

    Returns:
        list: List of centerpoints.
    """
    existing_timestampts = defaultdict(list)
    previous_location = defaultdict(list)

    centerpoints_dict = defaultdict(list)
     # Filter and combine the data
    for item in farsight_json_data:
        class_label, y_coord, x_coord, timestamp, is_alive = item
        is_duplicate = timestamp in existing_timestampts[class_label]
        has_stopped = f"{x_coord}, {y_coord}" == previous_location[class_label]
        if is_alive and not is_duplicate and not has_stopped:  # Only include alive points
            centerpoints_dict[class_label].append((x_coord, y_coord))
            existing_timestampts[class_label].append(timestamp)
            previous_location[class_label] = f"{x_coord}, {y_coord}"

    return centerpoints_dict
