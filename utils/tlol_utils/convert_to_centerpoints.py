from collections import defaultdict

from typedefs.centerpoint import Centerpoint

def convert_to_centerpoints(df, existing_classes=[]):
    """
    Convert TLoL gameobject data to centerpoints

    Args:
        bounding_boxes (list): List of champion game objects.

    Returns:
        list: List of centerpoints.
    """
    classes = existing_classes
    centerpoints_dict = defaultdict(list)
     # Filter and combine the data
    values = df[["name", "pos_x", "pos_z", "time", "hp", "team", "game_id"]].values.tolist()
    for value in values:
        name, y_coord, x_coord, timestamp, hp, team, game_id = value
        if name not in classes:
            classes.append(name)
        class_label = classes.index(name)
        is_alive = hp > 0
        if is_alive:  # Only include alive points
            centerpoint = Centerpoint({"classid": class_label, "point": [x_coord, y_coord], "timestamp": timestamp, "health": hp, "gameid": game_id, "teamid": team})
            centerpoints_dict[class_label].append(centerpoint)

    return centerpoints_dict, classes
