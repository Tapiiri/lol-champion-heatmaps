import numpy as np
import argparse
import math
from utils.deep_league_utils.convert_to_centerpoints import convert_to_centerpoints
from utils.get_file_paths import get_file_paths
from utils.get_output_path import get_output_path
from utils.save_centerpoints_as_npz import save_centerpoints_as_npz
from utils.save_class_labels_as_txt import save_class_labels_as_txt
from utils.tlol_utils.load_and_combine_tlol_db import load_and_combine_tlol_db
from utils.tlol_utils.convert_to_centerpoints import convert_to_centerpoints

def create_npz_from_tlol_db(dataset, output_file):
    """
    Save the centerpoints and their corresponding class labels as an NPZ file.

    Args:
        dataset (str): JSON file with the data points collected with Farsight.
        output_file (str): Path to the output NPZ file.
    """
    # Filter out the data points where the point is not alive
    alive_data = [data for data in dataset if data[4] is True]
    
    # Extract classes and centerpoints, discarding timestamps and alive status
    classes = np.array([data[0] for data in alive_data])
    centerpoints = np.array([[data[1], data[2]] for data in alive_data])
    
    # Save the filtered data to an NPZ file
    np.savez(output_file, classes=classes, centerpoints=centerpoints)
    print(f"NPZ file created at: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Convert a TLoL generated DB file .')
    parser.add_argument('-o', '--output-path', type=str, default='output.npz',
                        help='Optional: Output folder for the NPZ file. Defaults to "output".')
    parser.add_argument('-f', '--file-names', nargs='+', help='List of DB filenames or a file containing DB filenames')
    parser.add_argument('-a', '--output-amount', type=int, default=10,
                        help='Optional: Amount of NPZ files to output. Defaults to 10.')
    args = parser.parse_args()

    file_names = args.file_names
    output_amount = args.output_amount
    db_file_paths = get_file_paths(file_names, target_file_type="db")
    output_path = get_output_path(args.output_path, default_filename="output", default_file_type="npz")

    all_classes = []
    
    db_files_per_output_file = math.ceil(len(db_file_paths) / output_amount)
    # Round up

    # Save the data in chunks of size output_amount
    for i in range(0, len(db_file_paths), db_files_per_output_file):
        j = i + db_files_per_output_file
        print(f"Processing files {i} to {j}")
        farsight_json_data = load_and_combine_tlol_db(db_file_paths[i:j])
        centerpoints_dict, classes = convert_to_centerpoints(farsight_json_data, all_classes)
        all_classes = classes
        save_centerpoints_as_npz(centerpoints_dict, output_path.replace(".npz", f"_{i}.npz"))

    save_class_labels_as_txt(all_classes, output_path.replace(".npz", f"_classes.txt"))



if __name__ == "__main__":
    main()
