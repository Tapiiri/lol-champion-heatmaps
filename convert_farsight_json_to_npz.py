import numpy as np
import argparse
from utils.deep_league_utils.convert_to_centerpoints import convert_to_centerpoints
from utils.get_file_paths import get_file_paths
from utils.save_centerpoints_as_npz import save_centerpoints_as_npz
from utils.farsight_utils.load_and_combine_farsight_json import load_and_combine_farsight_json
from utils.farsight_utils.convert_to_centerpoints import convert_to_centerpoints

def create_npz_from_farsight_json(dataset, output_file):
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
    parser = argparse.ArgumentParser(description='Convert a Farsight generated JSON .')
    parser.add_argument('-o', '--output-path', type=str, default='output.npz',
                        help='Optional: Output folder for the NPZ file. Defaults to "output".')
    parser.add_argument('-f', '--file-names', nargs='+', help='List of JSON filenames or a file containing NPZ filenames')
    args = parser.parse_args()

    file_names = args.file_names
    json_file_paths = get_file_paths(file_names, target_file_type="json")
     
    farsight_json_data = load_and_combine_farsight_json(json_file_paths)
    centerpoints_dict = convert_to_centerpoints(farsight_json_data)

    save_centerpoints_as_npz(centerpoints_dict, args.output_path)


if __name__ == "__main__":
    main()
