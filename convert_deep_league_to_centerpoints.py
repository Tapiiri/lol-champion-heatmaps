import argparse
from utils.deep_league_utils.convert_to_centerpoints import convert_to_centerpoints
from utils.get_file_paths import get_file_paths
from utils.deep_league_utils.load_and_combine_npz_bounding_boxes import load_and_combine_npz_bounding_boxes
from utils.save_centerpoints_as_npz import save_centerpoints_as_npz

def main():
    parser = argparse.ArgumentParser(description='Overlay heatmap on map and save as an image.')
    parser.add_argument('-o', '--output-path', type=str, default='output.npz',
                        help='Optional: Output folder for the saved heatmap image. Defaults to "output".')
    parser.add_argument('-f', '--file-names', nargs='+', help='List of NPZ filenames or a file containing NPZ filenames')
    parser.add_argument('-c', '--class-names', type=str, help='List of NPZ class names in sequential order (eq. first class name is for class 0)')
    args = parser.parse_args()

    file_names = args.file_names
    npz_file_paths = get_file_paths(file_names, "npz")
     
    bounding_boxes_with_labels = load_and_combine_npz_bounding_boxes(npz_file_paths)
    centerpoints_dict = convert_to_centerpoints(bounding_boxes_with_labels)

    save_centerpoints_as_npz(centerpoints_dict, args.output_path)


if __name__ == "__main__":
    main()
