from collections import defaultdict

def convert_to_centerpoints(bounding_boxes):
    """
    Convert bounding boxes to centerpoints.

    Args:
        bounding_boxes (list): List of bounding boxes.

    Returns:
        list: List of centerpoints.
    """
    centerpoints_dict = defaultdict(list)
    for boxes in bounding_boxes:
        for box in boxes:
            class_label = box[0]
            x_center = (box[1] + box[3]) / 2  # Average of x_min and x_max
            y_center = (box[2] + box[4]) / 2  # Average of y_min and y_max
            centerpoints_dict[class_label].append((x_center, y_center))
    return centerpoints_dict
