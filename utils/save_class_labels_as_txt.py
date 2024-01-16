import numpy as np

def save_class_labels_as_txt(classes, output_file):
    """
    Save the class labels as a text file.

    Args:
        classes (list): List of class labels.
        output_file (str): Path to the output text file.
    """
    with open(output_file, "w") as f:
        for class_label in classes:
            f.write(f"{class_label}\n")
    print(f"Saved {len(classes)} class labels to {output_file}")